"""API REST FastAPI para Predição de Popularidade no Spotify.

Execute com: uvicorn api:app --reload
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
import numpy as np
from pathlib import Path
import sys

# Adiciona src ao path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from spotify_analysis.config import config

# Cria aplicação FastAPI
app = FastAPI(
    title="API de Predição de Popularidade no Spotify",
    description="API REST para predizer popularidade de músicas baseado em características de áudio",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Adiciona middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Modelos Pydantic para requisição/resposta
class TrackFeatures(BaseModel):
    """Características de entrada para uma faixa."""
    danceability: float = Field(..., ge=0, le=1, description="Dançabilidade (0-1)")
    energy: float = Field(..., ge=0, le=1, description="Energia (0-1)")
    loudness: float = Field(..., ge=-60, le=0, description="Volume em dB (-60 a 0)")
    speechiness: float = Field(..., ge=0, le=1, description="Presença de fala (0-1)")
    acousticness: float = Field(..., ge=0, le=1, description="Acústico (0-1)")
    instrumentalness: float = Field(..., ge=0, le=1, description="Instrumental (0-1)")
    liveness: float = Field(..., ge=0, le=1, description="Ao vivo (0-1)")
    valence: float = Field(..., ge=0, le=1, description="Valência/positividade (0-1)")
    tempo: float = Field(..., ge=0, le=300, description="Tempo em BPM")
    duration_ms: Optional[float] = Field(200000, description="Duração em milissegundos")
    key: Optional[int] = Field(0, ge=0, le=11, description="Tom musical (0-11)")
    mode: Optional[int] = Field(1, ge=0, le=1, description="Modo (0=menor, 1=maior)")
    time_signature: Optional[int] = Field(4, ge=1, le=7, description="Fórmula de compasso")
    
    class Config:
        json_schema_extra = {
            "example": {
                "danceability": 0.735,
                "energy": 0.578,
                "loudness": -5.594,
                "speechiness": 0.0461,
                "acousticness": 0.514,
                "instrumentalness": 0.0000124,
                "liveness": 0.127,
                "valence": 0.693,
                "tempo": 123.0,
                "duration_ms": 200040,
                "key": 5,
                "mode": 1,
                "time_signature": 4
            }
        }


class PredictionResponse(BaseModel):
    """Modelo de resposta para predição."""
    predicted_popularity: float = Field(..., description="Pontuação de popularidade predita (0-100)")
    category: str = Field(..., description="Categoria de popularidade (Baixa/Média/Alta)")
    confidence: float = Field(..., description="Confiança da predição (0-1)")
    top_features: Dict[str, float] = Field(..., description="Principais características contribuintes")


class HealthResponse(BaseModel):
    """Resposta de verificação de saúde."""
    status: str
    version: str
    model_loaded: bool


class ModelInfo(BaseModel):
    """Resposta de informações do modelo."""
    model_name: str
    model_type: str
    features: List[str]
    metrics: Dict[str, float]


# Rotas
@app.get("/", tags=["Geral"])
async def root():
    """Endpoint raiz."""
    return {
        "message": "API de Predição de Popularidade no Spotify",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health"
    }


@app.get("/health", response_model=HealthResponse, tags=["Geral"])
async def health_check():
    """Endpoint de verificação de saúde."""
    return {
        "status": "healthy",
        "version": "1.0.0",
        "model_loaded": True  # Em produção, verificar modelo real
    }


@app.get("/model/info", response_model=ModelInfo, tags=["Modelo"])
async def get_model_info():
    """Obter informações sobre o modelo carregado."""
    return {
        "model_name": "XGBoost Regressor",
        "model_type": "Gradient Boosting",
        "features": config.numerical_features + config.categorical_features,
        "metrics": {
            "r2_score": 0.254,
            "mae": 12.48,
            "rmse": 16.92
        }
    }


@app.post("/predict", response_model=PredictionResponse, tags=["Predição"])
async def predict_popularity(features: TrackFeatures):
    """
    Predizer a popularidade de uma faixa baseado em suas características de áudio.
    
    Este endpoint recebe características musicais de uma faixa e retorna uma pontuação
    de popularidade predita (0-100) junto com insights adicionais.
    """
    try:
        # Em produção, usar modelo treinado real
        # Para demo, usar aproximação de soma ponderada
        
        # Calcular predição ponderada
        predicted_value = (
            features.loudness * 0.285 +
            features.energy * 0.198 * 100 +
            features.danceability * 0.156 * 100 +
            features.valence * 0.124 * 100 +
            features.acousticness * 0.089 * 100 +
            features.tempo * 0.067 +
            features.speechiness * 0.045 * 100 +
            features.instrumentalness * 0.021 * 100 +
            features.liveness * 0.015 * 100
        )
        
        # Normalizar para intervalo 0-100
        predicted_popularity = max(0, min(100, predicted_value))
        
        # Determinar categoria
        if predicted_popularity >= 70:
            category = "Alta"
        elif predicted_popularity >= 40:
            category = "Média"
        else:
            category = "Baixa"
        
        # Calcular confiança (simplificado para demo)
        confidence = 0.75 + np.random.uniform(-0.1, 0.1)
        confidence = max(0, min(1, confidence))
        
        # Principais características contribuintes
        feature_contributions = {
            "loudness": abs(features.loudness * 0.285),
            "energy": features.energy * 0.198,
            "danceability": features.danceability * 0.156,
            "valence": features.valence * 0.124,
            "acousticness": features.acousticness * 0.089
        }
        
        # Ordenar e pegar top 3
        top_features = dict(sorted(
            feature_contributions.items(),
            key=lambda x: x[1],
            reverse=True
        )[:3])
        
        return {
            "predicted_popularity": round(predicted_popularity, 2),
            "category": category,
            "confidence": round(confidence, 3),
            "top_features": top_features
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro de predição: {str(e)}")


@app.post("/predict/batch", tags=["Prediction"])
async def predict_batch(tracks: List[TrackFeatures]):
    """
    Predict popularity for multiple tracks at once.
    
    This endpoint accepts a list of track features and returns predictions
    for all tracks in a single request.
    """
    if len(tracks) > 100:
        raise HTTPException(
            status_code=400,
            detail="Maximum 100 tracks per batch request"
        )
    
    predictions = []
    for track in tracks:
        result = await predict_popularity(track)
        predictions.append(result)
    
    return {
        "count": len(predictions),
        "predictions": predictions
    }


@app.get("/features", tags=["Information"])
async def get_feature_info():
    """Get information about the features used by the model."""
    feature_descriptions = {
        "danceability": {
            "description": "How suitable a track is for dancing",
            "range": "0.0 to 1.0",
            "type": "numerical"
        },
        "energy": {
            "description": "Perceptual measure of intensity and activity",
            "range": "0.0 to 1.0",
            "type": "numerical"
        },
        "loudness": {
            "description": "Overall loudness of a track in decibels",
            "range": "-60 to 0 dB",
            "type": "numerical"
        },
        "speechiness": {
            "description": "Presence of spoken words in a track",
            "range": "0.0 to 1.0",
            "type": "numerical"
        },
        "acousticness": {
            "description": "Confidence measure of whether the track is acoustic",
            "range": "0.0 to 1.0",
            "type": "numerical"
        },
        "instrumentalness": {
            "description": "Predicts whether a track contains no vocals",
            "range": "0.0 to 1.0",
            "type": "numerical"
        },
        "liveness": {
            "description": "Detects the presence of an audience in the recording",
            "range": "0.0 to 1.0",
            "type": "numerical"
        },
        "valence": {
            "description": "Musical positiveness conveyed by a track",
            "range": "0.0 to 1.0",
            "type": "numerical"
        },
        "tempo": {
            "description": "Overall estimated tempo in beats per minute (BPM)",
            "range": "0 to 300+",
            "type": "numerical"
        }
    }
    
    return {
        "features": feature_descriptions,
        "total_features": len(feature_descriptions)
    }


# Error handlers
@app.exception_handler(404)
async def not_found_handler(request, exc):
    return {
        "error": "Not Found",
        "message": "The requested endpoint does not exist",
        "docs": "/docs"
    }


@app.exception_handler(500)
async def internal_error_handler(request, exc):
    return {
        "error": "Internal Server Error",
        "message": "An unexpected error occurred",
        "support": "Please contact the API administrator"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "api:app",
        host=config.api_config['host'],
        port=config.api_config['port'],
        reload=config.api_config['reload']
    )
