"""
Script para treinar o Ridge Pipeline e gerar previsões
Utiliza dados X_train, y_train e X_test já definidos
"""

from ridge_pipeline import ridge_pipeline
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import numpy as np
import joblib
from datetime import datetime

# Assumindo que X_train, y_train e X_test já estão carregados
# Se precisar carregar, descomente as linhas abaixo: 
# import pandas as pd
# X_train = pd.read_csv('X_train.csv')
# y_train = pd.read_csv('y_train.csv')
# X_test = pd.read_csv('X_test.csv')

def train_ridge_model(X_train, y_train, X_test):
    """
    Treina o Ridge Pipeline e gera previsões
    
    Parameters:
    -----------
    X_train : DataFrame
        Features de treino
    y_train :  Series ou array
        Target de treino
    X_test : DataFrame
        Features de teste
        
    Returns:
    --------
    y_pred_ridge : array
        Previsões do modelo no conjunto de teste
    """
    
    print("="*60)
    print("TREINAMENTO DO RIDGE PIPELINE")
    print("="*60)
    
    # Informações sobre os dados
    print(f"\nShape dos dados de treino: {X_train.shape}")
    print(f"Shape dos dados de teste:  {X_test.shape}")
    print(f"Shape do target: {y_train.shape if hasattr(y_train, 'shape') else len(y_train)}")
    
    # Treinando o pipeline
    print("\n🔄 Treinando o modelo Ridge...")
    start_time = datetime.now()
    
    ridge_pipeline.fit(X_train, y_train)
    
    end_time = datetime.now()
    training_time = (end_time - start_time).total_seconds()
    
    print(f"✅ Modelo treinado com sucesso em {training_time:.2f} segundos!")
    
    # Gerando previsões
    print("\n🔮 Gerando previsões para X_test...")
    y_pred_ridge = ridge_pipeline.predict(X_test)
    
    print(f"✅ Previsões geradas!  Shape: {y_pred_ridge.shape}")
    
    # Informações sobre o modelo treinado
    print("\n" + "="*60)
    print("INFORMAÇÕES DO MODELO TREINADO")
    print("="*60)
    
    ridge_model = ridge_pipeline.named_steps['regressor']
    print(f"\nAlpha (regularização): {ridge_model.alpha}")
    print(f"Número de features após preprocessamento: {len(ridge_model.coef_)}")
    print(f"Intercepto:  {ridge_model.intercept_:.4f}")
    
    # Estatísticas dos coeficientes
    print(f"\nEstatísticas dos coeficientes:")
    print(f"  - Mínimo: {np.min(ridge_model.coef_):.4f}")
    print(f"  - Máximo: {np.max(ridge_model.coef_):.4f}")
    print(f"  - Média: {np.mean(ridge_model.coef_):.4f}")
    print(f"  - Desvio padrão: {np.std(ridge_model.coef_):.4f}")
    
    # Estatísticas das previsões
    print(f"\nEstatísticas das previsões:")
    print(f"  - Mínimo:  {np.min(y_pred_ridge):.4f}")
    print(f"  - Máximo: {np.max(y_pred_ridge):.4f}")
    print(f"  - Média: {np.mean(y_pred_ridge):.4f}")
    print(f"  - Desvio padrão: {np.std(y_pred_ridge):.4f}")
    
    # Salvando o modelo treinado
    model_filename = f'ridge_pipeline_trained_{datetime.now().strftime("%Y%m%d_%H%M%S")}.pkl'
    print(f"\n💾 Salvando modelo treinado como '{model_filename}'...")
    joblib.dump(ridge_pipeline, model_filename)
    print("✅ Modelo salvo com sucesso!")
    
    # Salvando as previsões
    predictions_filename = f'y_pred_ridge_{datetime.now().strftime("%Y%m%d_%H%M%S")}.npy'
    print(f"\n💾 Salvando previsões como '{predictions_filename}'...")
    np.save(predictions_filename, y_pred_ridge)
    print("✅ Previsões salvas com sucesso!")
    
    print("\n" + "="*60)
    
    return y_pred_ridge


def evaluate_predictions(y_train, y_pred_train, y_test=None, y_pred_test=None):
    """
    Avalia as previsões do modelo (opcional)
    
    Parameters: 
    -----------
    y_train :  array
        Target real de treino
    y_pred_train : array
        Previsões de treino
    y_test :  array, optional
        Target real de teste
    y_pred_test : array, optional
        Previsões de teste
    """
    print("\n" + "="*60)
    print("AVALIAÇÃO DO MODELO (TREINO)")
    print("="*60)
    
    mse_train = mean_squared_error(y_train, y_pred_train)
    rmse_train = np.sqrt(mse_train)
    mae_train = mean_absolute_error(y_train, y_pred_train)
    r2_train = r2_score(y_train, y_pred_train)
    
    print(f"\nMétricas no conjunto de treino:")
    print(f"  - MSE:   {mse_train:.4f}")
    print(f"  - RMSE: {rmse_train:.4f}")
    print(f"  - MAE:  {mae_train:.4f}")
    print(f"  - R²:   {r2_train:.4f}")
    
    if y_test is not None and y_pred_test is not None:
        print("\n" + "="*60)
        print("AVALIAÇÃO DO MODELO (TESTE)")
        print("="*60)
        
        mse_test = mean_squared_error(y_test, y_pred_test)
        rmse_test = np.sqrt(mse_test)
        mae_test = mean_absolute_error(y_test, y_pred_test)
        r2_test = r2_score(y_test, y_pred_test)
        
        print(f"\nMétricas no conjunto de teste:")
        print(f"  - MSE:  {mse_test:.4f}")
        print(f"  - RMSE: {rmse_test:.4f}")
        print(f"  - MAE:  {mae_test:.4f}")
        print(f"  - R²:   {r2_test:.4f}")
        
        # Análise de overfitting/underfitting
        print(f"\n📊 Análise:")
        diff_r2 = r2_train - r2_test
        if diff_r2 > 0.1:
            print(f"  ⚠️  Possível overfitting (diferença R²: {diff_r2:.4f})")
        elif r2_train < 0.5 and r2_test < 0.5:
            print(f"  ⚠️  Possível underfitting (R² baixo em ambos)")
        else:
            print(f"  ✅ Modelo bem balanceado (diferença R²: {diff_r2:.4f})")


if __name__ == "__main__":
    # Treinar o modelo e gerar previsões
    y_pred_ridge = train_ridge_model(X_train, y_train, X_test)
    
    # Se você também tiver y_test e quiser avaliar: 
    # y_pred_train = ridge_pipeline.predict(X_train)
    # evaluate_predictions(y_train, y_pred_train, y_test, y_pred_ridge)
    
    print("\n✨ Processo concluído com sucesso!")
    print(f"📌 Use 'y_pred_ridge' para suas análises")
