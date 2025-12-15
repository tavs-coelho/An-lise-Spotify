# Demo Video & Screenshots

## 🎥 Demo Video Instructions

Since we cannot create an actual video file in this environment, here's a comprehensive guide for creating a demo video:

### Suggested Demo Script (3-5 minutes)

#### 1. Introduction (30 seconds)
- Show the GitHub repository homepage
- Highlight the professional README with badges
- Mention the production-ready architecture

#### 2. Project Overview (30 seconds)
- Show the architecture diagram
- Explain the three main interfaces: API, Dashboard, Library
- Mention key technologies: FastAPI, Streamlit, Docker, XGBoost

#### 3. FastAPI Demo (60 seconds)
**Steps to record:**
```bash
# Start the API
docker-compose up -d api
# Or: uvicorn api:app --reload
```

- Open browser to `http://localhost:8000/docs`
- Show the interactive Swagger UI
- Demonstrate the `/health` endpoint (click "Try it out")
- Show the `/predict` endpoint with sample data
- Execute a prediction request
- Display the JSON response with predicted popularity

**Sample prediction request:**
```json
{
  "danceability": 0.735,
  "energy": 0.578,
  "loudness": -5.594,
  "speechiness": 0.0461,
  "acousticness": 0.514,
  "instrumentalness": 0.0000124,
  "liveness": 0.127,
  "valence": 0.693,
  "tempo": 123.0
}
```

#### 4. Streamlit Dashboard Demo (90 seconds)
**Steps to record:**
```bash
# Start the dashboard
streamlit run app.py
```

- Open browser to `http://localhost:8501`
- **Overview Page:**
  - Show the metrics cards
  - Scroll through popularity distribution chart
  
- **Data Explorer:**
  - Display sample data table
  - Show feature statistics
  - Display correlation heatmap
  
- **Model Performance:**
  - Compare different models (XGBoost, Random Forest, etc.)
  - Show R² and MAE comparisons
  
- **Feature Analysis:**
  - Display feature importance chart
  - Show scatter plots of feature relationships
  
- **Make Predictions:**
  - Adjust sliders for different features
  - Click "Predict Popularity"
  - Show the gauge chart with prediction result

#### 5. Python Library Usage (30 seconds)
**Show code in Jupyter or terminal:**
```python
from spotify_analysis.models import ModelTrainer
from spotify_analysis.data import DataLoader

# Load data
loader = DataLoader()
# (Note: Will use sample data if CSV not available)

# Train model
trainer = ModelTrainer('xgboost')
# trainer.fit(X_train, y_train)

# Make predictions
# predictions = trainer.predict(X_test)
```

#### 6. Docker Demo (20 seconds)
**Show in terminal:**
```bash
# Start all services with one command
docker-compose up -d

# Show running containers
docker ps

# Show logs
docker-compose logs -f
```

#### 7. Code Quality (20 seconds)
- Show the test suite: `pytest`
- Show code formatting: `black src/`
- Show linting: `flake8 src/`
- Mention CI/CD pipeline (show GitHub Actions)

#### 8. Closing (20 seconds)
- Highlight key achievements:
  - ✅ Production-ready ML system
  - ✅ Multiple interfaces (API, Dashboard, Library)
  - ✅ Comprehensive testing and documentation
  - ✅ Docker deployment
  - ✅ CI/CD pipeline
- Show the GitHub repository with star button
- Display contact information

---

## 📸 Screenshots

All screenshots have been generated and are available in `assets/screenshots/`:

1. **dashboard_preview.png** - Streamlit dashboard interface with metrics, charts, and predictions
2. **api_preview.png** - FastAPI REST API documentation with endpoints
3. **architecture.png** - System architecture diagram showing all components
4. **results_summary.png** - Model performance comparison and key insights
5. **feature_analysis.png** - Feature importance and correlation analysis

---

## 🛠️ Tools for Creating Demo Video

### Option 1: Screen Recording Tools
- **OBS Studio** (Free, cross-platform)
- **Loom** (Free tier available, easy to use)
- **QuickTime** (Mac)
- **Windows Game Bar** (Windows)
- **SimpleScreenRecorder** (Linux)

### Option 2: Animated GIF
Create an animated GIF using:
- **LICEcap** (Windows/Mac)
- **Peek** (Linux)
- **ScreenToGif** (Windows)

### Option 3: Professional Tools
- **Camtasia** (Paid, professional editing)
- **Adobe Premiere** (Paid, advanced editing)
- **DaVinci Resolve** (Free version available)

---

## 📝 Recording Tips

1. **Preparation:**
   - Close unnecessary browser tabs and applications
   - Set browser zoom to 100%
   - Use full-screen or maximize windows
   - Clear terminal history

2. **During Recording:**
   - Speak clearly and at a moderate pace
   - Use smooth mouse movements
   - Allow 2-3 seconds pause between actions
   - Highlight cursor when clicking (many tools have this feature)

3. **Audio:**
   - Use a good microphone or headset
   - Record in a quiet environment
   - Consider adding background music (royalty-free)

4. **Post-Production:**
   - Add captions or text overlays for key points
   - Speed up slow sections (e.g., installing dependencies)
   - Add transitions between sections
   - Include intro/outro screens with title and credits

---

## 🎬 Alternative: Create GIF Demos

For quick demonstrations without audio, create GIFs:

1. **API Demo GIF:**
   - Show opening Swagger UI
   - Executing a prediction
   - Viewing the response

2. **Dashboard Demo GIF:**
   - Navigate through different pages
   - Adjust sliders for prediction
   - Show the gauge chart animation

3. **Docker Demo GIF:**
   - Run `docker-compose up -d`
   - Show `docker ps`
   - Open browser to both services

---

## 📤 Publishing Your Demo

Once recorded, upload to:
- **YouTube** (public or unlisted)
- **Vimeo**
- **GitHub Release** (if file size permits)
- **Loom** (shareable link)

Then update the README with:
```markdown
## 🎥 Demo Video

Watch our 5-minute demo showcasing all features:

[![Demo Video](assets/screenshots/dashboard_preview.png)](YOUR_VIDEO_URL)

Or view it directly: [Demo Video Link](YOUR_VIDEO_URL)
```

---

## 📊 Using the Screenshots

The generated screenshots are ready to use in:
- README.md
- Documentation
- Presentations
- Academic reports
- Project portfolio

They are high-resolution (150 DPI) and saved as PNG for quality.
