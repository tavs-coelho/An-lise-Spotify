"""Dashboard Streamlit para Análise de Popularidade de Músicas no Spotify.

Execute com: streamlit run app.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
import sys

# Adiciona src ao path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from spotify_analysis.config import config
from spotify_analysis.data import DataLoader
from spotify_analysis.models import ModelTrainer
from spotify_analysis.visualization import (
    plot_distribution,
    plot_correlation_heatmap,
    plot_feature_importance,
    plot_predictions_vs_actual
)

# Configuração da página
st.set_page_config(
    page_title=config.streamlit_config['page_title'],
    page_icon=config.streamlit_config['page_icon'],
    layout=config.streamlit_config['layout']
)

# CSS personalizado
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1DB954;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        font-weight: bold;
        color: #1DB954;
        margin-top: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1DB954;
    }
</style>
""", unsafe_allow_html=True)

# Título
st.markdown('<h1 class="main-header">🎵 Análise de Popularidade de Músicas no Spotify</h1>', unsafe_allow_html=True)
st.markdown("### Dashboard Interativo para Análise de Machine Learning")

# Barra lateral
st.sidebar.image("https://storage.googleapis.com/pr-newsroom-wp/1/2018/11/Spotify_Logo_RGB_Green.png", width=200)
st.sidebar.title("Navegação")
page = st.sidebar.radio("Ir para", [
    "📊 Visão Geral",
    "🔍 Explorador de Dados",
    "🤖 Desempenho do Modelo",
    "📈 Análise de Features",
    "🎯 Fazer Predições"
])

st.sidebar.markdown("---")
st.sidebar.info(
    "**Sobre:** Este dashboard fornece uma interface interativa para explorar "
    "o modelo de predição de popularidade de músicas no Spotify."
)

# Dados de exemplo para demo (em produção, carregar dados reais)
@st.cache_data
def load_sample_data():
    """Carregar dados de exemplo para demonstração."""
    np.random.seed(42)
    n_samples = 1000
    
    data = {
        'danceability': np.random.uniform(0, 1, n_samples),
        'energy': np.random.uniform(0, 1, n_samples),
        'loudness': np.random.uniform(-60, 0, n_samples),
        'speechiness': np.random.uniform(0, 1, n_samples),
        'acousticness': np.random.uniform(0, 1, n_samples),
        'instrumentalness': np.random.uniform(0, 1, n_samples),
        'liveness': np.random.uniform(0, 1, n_samples),
        'valence': np.random.uniform(0, 1, n_samples),
        'tempo': np.random.uniform(60, 200, n_samples),
        'track_popularity': np.random.randint(0, 100, n_samples)
    }
    
    return pd.DataFrame(data)

df = load_sample_data()

# PÁGINA: Visão Geral
if page == "📊 Visão Geral":
    st.markdown('<h2 class="sub-header">Visão Geral do Projeto</h2>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Songs", f"{len(df):,}", help="Number of songs in dataset")
    with col2:
        st.metric("Features", "10", help="Number of musical features")
    with col3:
        st.metric("Best Model", "XGBoost", help="Highest performing model")
    with col4:
        st.metric("R² Score", "0.254", help="Model explanation power")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🎯 Project Goals")
        st.markdown("""
        - Predict music popularity based on audio features
        - Identify key factors influencing popularity
        - Compare multiple ML algorithms
        - Provide actionable insights for artists and producers
        """)
    
    with col2:
        st.markdown("#### 🛠️ Technologies Used")
        st.markdown("""
        - **ML:** scikit-learn, XGBoost
        - **Data:** Pandas, NumPy
        - **Viz:** Matplotlib, Seaborn, Plotly
        - **Web:** Streamlit, FastAPI
        """)
    
    st.markdown("---")
    st.markdown("#### 📊 Popularity Distribution")
    
    fig = px.histogram(
        df,
        x='track_popularity',
        nbins=50,
        title='Distribution of Track Popularity',
        labels={'track_popularity': 'Popularity Score'},
        color_discrete_sequence=['#1DB954']
    )
    fig.update_layout(showlegend=False, height=400)
    st.plotly_chart(fig, use_container_width=True)

# PAGE: Data Explorer
elif page == "🔍 Data Explorer":
    st.markdown('<h2 class="sub-header">Data Explorer</h2>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["📋 Dataset", "📊 Statistics", "🔗 Correlations"])
    
    with tab1:
        st.markdown("#### Sample Data")
        st.dataframe(df.head(100), use_container_width=True)
        
        st.download_button(
            label="📥 Download Data (CSV)",
            data=df.to_csv(index=False).encode('utf-8'),
            file_name='spotify_sample_data.csv',
            mime='text/csv'
        )
    
    with tab2:
        st.markdown("#### Statistical Summary")
        st.dataframe(df.describe(), use_container_width=True)
        
        st.markdown("#### Feature Distributions")
        selected_feature = st.selectbox("Select feature to visualize", df.columns[:-1])
        
        fig = px.histogram(
            df,
            x=selected_feature,
            nbins=50,
            title=f'Distribution of {selected_feature}',
            color_discrete_sequence=['#1DB954']
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.markdown("#### Correlation Matrix")
        
        corr_matrix = df.corr()
        
        fig = px.imshow(
            corr_matrix,
            labels=dict(color="Correlation"),
            x=corr_matrix.columns,
            y=corr_matrix.columns,
            color_continuous_scale='RdBu_r',
            aspect='auto',
            title='Feature Correlation Heatmap'
        )
        fig.update_layout(height=600)
        st.plotly_chart(fig, use_container_width=True)

# PAGE: Model Performance
elif page == "🤖 Model Performance":
    st.markdown('<h2 class="sub-header">Model Performance Comparison</h2>', unsafe_allow_html=True)
    
    # Sample model results
    models_data = {
        'Model': ['XGBoost', 'Gradient Boosting', 'Random Forest', 'Ridge', 'Lasso', 'ElasticNet'],
        'R² Score': [0.254, 0.241, 0.228, 0.182, 0.179, 0.185],
        'MAE': [12.48, 12.73, 13.02, 14.35, 14.48, 14.21],
        'RMSE': [16.92, 17.15, 17.48, 19.01, 19.12, 18.92]
    }
    
    models_df = pd.DataFrame(models_data)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### R² Score Comparison")
        fig = px.bar(
            models_df,
            x='Model',
            y='R² Score',
            color='R² Score',
            color_continuous_scale='Greens',
            title='R² Score by Model (Higher is Better)'
        )
        fig.update_layout(showlegend=False, height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("#### MAE Comparison")
        fig = px.bar(
            models_df,
            x='Model',
            y='MAE',
            color='MAE',
            color_continuous_scale='Reds_r',
            title='Mean Absolute Error by Model (Lower is Better)'
        )
        fig.update_layout(showlegend=False, height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    st.markdown("#### Detailed Metrics")
    st.dataframe(models_df, use_container_width=True)

# PAGE: Feature Analysis
elif page == "📈 Feature Analysis":
    st.markdown('<h2 class="sub-header">Feature Importance Analysis</h2>', unsafe_allow_html=True)
    
    # Sample feature importance
    importance_data = {
        'Feature': ['loudness', 'energy', 'danceability', 'valence', 'acousticness',
                   'tempo', 'speechiness', 'instrumentalness', 'liveness'],
        'Importance': [0.285, 0.198, 0.156, 0.124, 0.089, 0.067, 0.045, 0.021, 0.015]
    }
    
    importance_df = pd.DataFrame(importance_data)
    
    fig = px.bar(
        importance_df,
        y='Feature',
        x='Importance',
        orientation='h',
        color='Importance',
        color_continuous_scale='Viridis',
        title='XGBoost Feature Importance'
    )
    fig.update_layout(showlegend=False, height=500)
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    st.markdown("#### Feature Relationships")
    
    col1, col2 = st.columns(2)
    
    with col1:
        feature_x = st.selectbox("Select X-axis feature", df.columns[:-1], index=0)
    with col2:
        feature_y = st.selectbox("Select Y-axis feature", df.columns[:-1], index=1)
    
    fig = px.scatter(
        df,
        x=feature_x,
        y=feature_y,
        color='track_popularity',
        color_continuous_scale='Viridis',
        title=f'{feature_x.title()} vs {feature_y.title()}',
        labels={'track_popularity': 'Popularity'},
        opacity=0.6
    )
    st.plotly_chart(fig, use_container_width=True)

# PAGE: Make Predictions
elif page == "🎯 Make Predictions":
    st.markdown('<h2 class="sub-header">Predict Track Popularity</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    Adjust the sliders below to set the musical features of a track, 
    and get a prediction of its popularity score (0-100).
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        danceability = st.slider("Danceability", 0.0, 1.0, 0.5, 0.01)
        energy = st.slider("Energy", 0.0, 1.0, 0.5, 0.01)
        loudness = st.slider("Loudness (dB)", -60.0, 0.0, -10.0, 1.0)
        speechiness = st.slider("Speechiness", 0.0, 1.0, 0.1, 0.01)
        acousticness = st.slider("Acousticness", 0.0, 1.0, 0.3, 0.01)
    
    with col2:
        instrumentalness = st.slider("Instrumentalness", 0.0, 1.0, 0.0, 0.01)
        liveness = st.slider("Liveness", 0.0, 1.0, 0.2, 0.01)
        valence = st.slider("Valence", 0.0, 1.0, 0.5, 0.01)
        tempo = st.slider("Tempo (BPM)", 60.0, 200.0, 120.0, 1.0)
    
    # Simple prediction simulation (in production, use trained model)
    if st.button("🎯 Predict Popularity", type="primary"):
        # Weighted sum for demo purposes
        predicted_popularity = (
            loudness * 0.285 +
            energy * 0.198 * 100 +
            danceability * 0.156 * 100 +
            valence * 0.124 * 100 +
            acousticness * 0.089 * 100 +
            tempo * 0.067 +
            speechiness * 0.045 * 100 +
            instrumentalness * 0.021 * 100 +
            liveness * 0.015 * 100
        )
        
        # Normalize to 0-100
        predicted_popularity = max(0, min(100, predicted_popularity))
        
        st.markdown("---")
        st.markdown("### Prediction Result")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            st.metric(
                label="Predicted Popularity Score",
                value=f"{predicted_popularity:.1f}",
                delta="Out of 100"
            )
            
            # Create gauge chart
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=predicted_popularity,
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': "Popularity Score"},
                gauge={
                    'axis': {'range': [0, 100]},
                    'bar': {'color': "#1DB954"},
                    'steps': [
                        {'range': [0, 33], 'color': "lightgray"},
                        {'range': [33, 66], 'color': "gray"},
                        {'range': [66, 100], 'color': "darkgray"}
                    ],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.75,
                        'value': 90
                    }
                }
            ))
            fig.update_layout(height=300)
            st.plotly_chart(fig, use_container_width=True)
        
        # Interpretation
        if predicted_popularity >= 70:
            category = "High"
            emoji = "🔥"
            message = "This track has strong commercial potential!"
        elif predicted_popularity >= 40:
            category = "Medium"
            emoji = "👍"
            message = "This track has moderate commercial potential."
        else:
            category = "Low"
            emoji = "💡"
            message = "This track may need more promotion or refinement."
        
        st.success(f"{emoji} **{category} Popularity** - {message}")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>🎵 Spotify Music Popularity Analysis Dashboard | Built with Streamlit</p>
    <p>GitHub: <a href='https://github.com/tavs-coelho/An-lise-Spotify'>tavs-coelho/An-lise-Spotify</a></p>
</div>
""", unsafe_allow_html=True)
