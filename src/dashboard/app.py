"""
Streamlit Dashboard for Spotify Music Analytics.
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import logging

from src.utils.config import load_config
from src.data.loader import DataLoader
from src.models.predictor import PopularityPredictor

# Configure logging
logger = logging.getLogger(__name__)

# Page configuration
st.set_page_config(
    page_title="Spotify Music Analytics",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1DB954;
        text-align: center;
        padding: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #191414;
        margin-top: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)


@st.cache_resource
def load_data_and_config():
    """Load configuration and data."""
    config = load_config('config.yaml')
    data_loader = DataLoader(config)
    df = data_loader.load_data()
    df_clean = data_loader.clean_data(df)
    return config, df_clean, data_loader


def main():
    """Main dashboard function."""
    
    # Header
    st.markdown('<h1 class="main-header">🎵 Spotify Music Analytics Dashboard</h1>', 
                unsafe_allow_html=True)
    st.markdown("---")
    
    # Load data
    try:
        config, df, data_loader = load_data_and_config()
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return
    
    # Sidebar
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Select Page",
        ["Overview", "Data Explorer", "Model Prediction", "Feature Analysis"]
    )
    
    if page == "Overview":
        show_overview(df, config)
    elif page == "Data Explorer":
        show_data_explorer(df)
    elif page == "Model Prediction":
        show_prediction_interface(config)
    elif page == "Feature Analysis":
        show_feature_analysis(df, config)


def show_overview(df: pd.DataFrame, config: dict):
    """Display overview page."""
    st.header("📊 Dataset Overview")
    
    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Tracks", f"{len(df):,}")
    with col2:
        st.metric("Features", len(config['features']['numerical']))
    with col3:
        st.metric("Avg Popularity", f"{df['popularity'].mean():.1f}")
    with col4:
        st.metric("Std Popularity", f"{df['popularity'].std():.1f}")
    
    # Popularity distribution
    st.subheader("Popularity Distribution")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.hist(df['popularity'], bins=50, color='#1DB954', alpha=0.7, edgecolor='black')
    ax.set_xlabel('Popularity Score')
    ax.set_ylabel('Frequency')
    ax.set_title('Distribution of Music Popularity')
    st.pyplot(fig)
    
    # Feature statistics
    st.subheader("Feature Statistics")
    numeric_cols = config['features']['numerical']
    numeric_cols = [col for col in numeric_cols if col in df.columns]
    st.dataframe(df[numeric_cols].describe().T, use_container_width=True)


def show_data_explorer(df: pd.DataFrame):
    """Display data explorer page."""
    st.header("🔍 Data Explorer")
    
    # Sample data
    st.subheader("Sample Data")
    n_samples = st.slider("Number of samples to display", 5, 50, 10)
    st.dataframe(df.head(n_samples), use_container_width=True)
    
    # Correlation heatmap
    st.subheader("Feature Correlation Heatmap")
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    
    if len(numeric_cols) > 1:
        fig, ax = plt.subplots(figsize=(12, 8))
        correlation = df[numeric_cols].corr()
        sns.heatmap(correlation, annot=True, fmt='.2f', cmap='coolwarm', 
                   center=0, ax=ax, cbar_kws={'label': 'Correlation'})
        ax.set_title('Feature Correlation Matrix')
        st.pyplot(fig)


def show_prediction_interface(config: dict):
    """Display prediction interface."""
    st.header("🎯 Popularity Prediction")
    
    st.info("Enter music features to predict popularity score (0-100)")
    
    # Create input form
    col1, col2 = st.columns(2)
    
    with col1:
        danceability = st.slider("Danceability", 0.0, 1.0, 0.5)
        energy = st.slider("Energy", 0.0, 1.0, 0.5)
        loudness = st.slider("Loudness (dB)", -60.0, 0.0, -10.0)
        speechiness = st.slider("Speechiness", 0.0, 1.0, 0.1)
        acousticness = st.slider("Acousticness", 0.0, 1.0, 0.5)
    
    with col2:
        instrumentalness = st.slider("Instrumentalness", 0.0, 1.0, 0.0)
        liveness = st.slider("Liveness", 0.0, 1.0, 0.1)
        valence = st.slider("Valence (Positivity)", 0.0, 1.0, 0.5)
        tempo = st.slider("Tempo (BPM)", 50, 200, 120)
        duration_ms = st.number_input("Duration (ms)", 60000, 600000, 200000)
    
    if st.button("Predict Popularity", type="primary"):
        try:
            # Create feature DataFrame
            features = pd.DataFrame([{
                'danceability': danceability,
                'energy': energy,
                'loudness': loudness,
                'speechiness': speechiness,
                'acousticness': acousticness,
                'instrumentalness': instrumentalness,
                'liveness': liveness,
                'valence': valence,
                'tempo': tempo,
                'duration_ms': duration_ms,
                'key': 0,
                'mode': 1,
                'time_signature': 4
            }])
            
            # Load model and predict
            predictor = PopularityPredictor(config)
            try:
                predictor.load_model('models/xgboost_model.pkl', 'XGBoost')
                prediction = predictor.predict(features, 'XGBoost')[0]
                
                # Display prediction
                st.success("Prediction Complete!")
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Predicted Popularity", f"{prediction:.1f}")
                with col2:
                    if prediction >= 67:
                        category = "High 🔥"
                    elif prediction >= 34:
                        category = "Medium ⭐"
                    else:
                        category = "Low 📊"
                    st.metric("Category", category)
                with col3:
                    percentile = int((prediction / 100) * 100)
                    st.metric("Percentile", f"{percentile}%")
                
                # Visualization
                fig, ax = plt.subplots(figsize=(8, 2))
                ax.barh(['Popularity'], [prediction], color='#1DB954')
                ax.set_xlim(0, 100)
                ax.set_xlabel('Popularity Score')
                ax.set_title('Predicted Popularity Score')
                for i, v in enumerate([prediction]):
                    ax.text(v + 1, i, f'{v:.1f}', va='center')
                st.pyplot(fig)
                
            except FileNotFoundError:
                st.error("Model not found. Please train the model first by running: python main.py")
        except Exception as e:
            st.error(f"Error making prediction: {e}")


def show_feature_analysis(df: pd.DataFrame, config: dict):
    """Display feature analysis page."""
    st.header("📈 Feature Analysis")
    
    # Select feature to analyze
    numeric_cols = config['features']['numerical']
    numeric_cols = [col for col in numeric_cols if col in df.columns]
    
    selected_feature = st.selectbox("Select Feature to Analyze", numeric_cols)
    
    if selected_feature:
        col1, col2 = st.columns(2)
        
        with col1:
            # Distribution plot
            st.subheader(f"{selected_feature.title()} Distribution")
            fig, ax = plt.subplots(figsize=(8, 5))
            ax.hist(df[selected_feature], bins=50, color='#1DB954', 
                   alpha=0.7, edgecolor='black')
            ax.set_xlabel(selected_feature.title())
            ax.set_ylabel('Frequency')
            st.pyplot(fig)
        
        with col2:
            # Scatter plot with popularity
            st.subheader(f"{selected_feature.title()} vs Popularity")
            fig, ax = plt.subplots(figsize=(8, 5))
            ax.scatter(df[selected_feature], df['popularity'], 
                      alpha=0.3, color='#1DB954', s=10)
            ax.set_xlabel(selected_feature.title())
            ax.set_ylabel('Popularity')
            
            # Add trend line
            z = np.polyfit(df[selected_feature], df['popularity'], 1)
            p = np.poly1d(z)
            ax.plot(df[selected_feature], p(df[selected_feature]), 
                   "r--", alpha=0.8, linewidth=2)
            st.pyplot(fig)
        
        # Statistics
        st.subheader("Statistics")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Mean", f"{df[selected_feature].mean():.3f}")
        with col2:
            st.metric("Median", f"{df[selected_feature].median():.3f}")
        with col3:
            st.metric("Std Dev", f"{df[selected_feature].std():.3f}")
        with col4:
            correlation = df[[selected_feature, 'popularity']].corr().iloc[0, 1]
            st.metric("Correlation with Popularity", f"{correlation:.3f}")


if __name__ == "__main__":
    main()
