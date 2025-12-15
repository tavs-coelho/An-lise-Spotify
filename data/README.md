# Data Directory

This directory contains the datasets used in the Spotify Music Popularity Analysis project.

## Dataset

### Spotify Songs Dataset

The main dataset used in this project is the **Spotify Songs** dataset, which contains audio features for thousands of tracks.

#### Download Instructions

Due to size limitations, the dataset is not included in this repository. Please download it using one of the following methods:

##### Option 1: Kaggle API (Recommended)

```bash
# Install Kaggle API
pip install kaggle

# Configure Kaggle credentials (place kaggle.json in ~/.kaggle/)
# Download the dataset
kaggle datasets download -d zaheenhamidani/ultimate-spotify-tracks-db

# Unzip to data directory
unzip ultimate-spotify-tracks-db.zip -d data/
```

##### Option 2: Manual Download

1. Visit [Kaggle - Ultimate Spotify Tracks DB](https://www.kaggle.com/datasets/zaheenhamidani/ultimate-spotify-tracks-db)
2. Download the CSV file
3. Place it in this directory as `spotify_songs.csv`

#### Dataset Information

- **Rows:** ~113,999 tracks
- **Columns:** 23 features
- **Size:** ~15 MB
- **Format:** CSV

## Sample Data

For testing purposes, the application can generate sample data if the main dataset is not available.
