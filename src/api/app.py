"""
FastAPI application for Spotify Popularity Prediction API.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Dict, Any
import numpy as np
import pandas as pd
from pathlib import Path
import sys

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent.parent))

from src.utils.config import load_config
from src.models.predictor import PopularityPredictor

# Load configuration
config = load_config('config.yaml')

# Initialize FastAPI app
app = FastAPI(
    title=config['api']['title'],
    version=config['api']['version'],
    description="API for predicting music popularity on Spotify based on audio features"
)

# Load model
predictor = PopularityPredictor(config)
try:
    predictor.load_model('models/xgboost_model.pkl', 'XGBoost')
except FileNotFoundError:
    print("Warning: Model file not found. Please train the model first.")


class MusicFeatures(BaseModel):
    """Schema for music features input."""
    
    danceability: float = Field(..., ge=0, le=1, description="How suitable for dancing (0-1)")
    energy: float = Field(..., ge=0, le=1, description="Intensity and activity (0-1)")
    loudness: float = Field(..., ge=-60, le=0, description="Overall loudness in dB")
    speechiness: float = Field(..., ge=0, le=1, description="Presence of spoken words (0-1)")
    acousticness: float = Field(..., ge=0, le=1, description="Acoustic confidence (0-1)")
    instrumentalness: float = Field(..., ge=0, le=1, description="No vocals prediction (0-1)")
    liveness: float = Field(..., ge=0, le=1, description="Audience presence (0-1)")
    valence: float = Field(..., ge=0, le=1, description="Musical positiveness (0-1)")
    tempo: float = Field(..., gt=0, le=300, description="Tempo in BPM")
    duration_ms: float = Field(..., gt=0, description="Track duration in milliseconds")
    key: int = Field(default=0, ge=0, le=11, description="Key (0-11)")
    mode: int = Field(default=1, ge=0, le=1, description="Mode (0=minor, 1=major)")
    time_signature: int = Field(default=4, ge=3, le=7, description="Time signature")
    
    class Config:
        schema_extra = {
            "example": {
                "danceability": 0.735,
                "energy": 0.578,
                "loudness": -11.84,
                "speechiness": 0.0598,
                "acousticness": 0.514,
                "instrumentalness": 0.0000234,
                "liveness": 0.0902,
                "valence": 0.636,
                "tempo": 121.274,
                "duration_ms": 200000,
                "key": 0,
                "mode": 1,
                "time_signature": 4
            }
        }


class PredictionResponse(BaseModel):
    """Schema for prediction response."""
    
    popularity: float = Field(..., description="Predicted popularity score (0-100)")
    confidence: str = Field(..., description="Prediction confidence level")
    category: str = Field(..., description="Popularity category")


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "message": "Spotify Music Popularity Prediction API",
        "version": config['api']['version'],
        "endpoints": {
            "/predict": "POST - Predict popularity for a single track",
            "/predict/batch": "POST - Predict popularity for multiple tracks",
            "/health": "GET - Health check"
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    model_loaded = 'XGBoost' in predictor.models
    return {
        "status": "healthy" if model_loaded else "model not loaded",
        "model_loaded": model_loaded
    }


@app.post("/predict", response_model=PredictionResponse)
async def predict_popularity(features: MusicFeatures):
    """
    Predict popularity for a single track.
    
    Args:
        features: Music features
        
    Returns:
        Prediction response with popularity score
    """
    if 'XGBoost' not in predictor.models:
        raise HTTPException(
            status_code=503,
            detail="Model not loaded. Please train the model first."
        )
    
    # Convert to DataFrame
    features_dict = features.dict()
    df = pd.DataFrame([features_dict])
    
    # Make prediction
    try:
        prediction = predictor.predict(df, 'XGBoost')[0]
        
        # Determine category and confidence
        if prediction >= 67:
            category = "High Popularity"
            confidence = "High"
        elif prediction >= 34:
            category = "Medium Popularity"
            confidence = "Medium"
        else:
            category = "Low Popularity"
            confidence = "High"
        
        return PredictionResponse(
            popularity=float(prediction),
            confidence=confidence,
            category=category
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/predict/batch")
async def predict_batch(features_list: List[MusicFeatures]):
    """
    Predict popularity for multiple tracks.
    
    Args:
        features_list: List of music features
        
    Returns:
        List of predictions
    """
    if 'XGBoost' not in predictor.models:
        raise HTTPException(
            status_code=503,
            detail="Model not loaded. Please train the model first."
        )
    
    predictions = []
    
    for features in features_list:
        features_dict = features.dict()
        df = pd.DataFrame([features_dict])
        
        try:
            prediction = predictor.predict(df, 'XGBoost')[0]
            
            if prediction >= 67:
                category = "High Popularity"
            elif prediction >= 34:
                category = "Medium Popularity"
            else:
                category = "Low Popularity"
            
            predictions.append({
                "popularity": float(prediction),
                "category": category
            })
        except Exception as e:
            predictions.append({
                "error": str(e)
            })
    
    return {"predictions": predictions}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app, 
        host=config['api']['host'], 
        port=config['api']['port']
    )
