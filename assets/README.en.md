# Assets Directory

This directory contains visual assets for the project documentation.

## 📁 Directory Structure

```
assets/
├── screenshots/          # High-resolution screenshots of the application
│   ├── dashboard_preview.png      # Streamlit dashboard interface
│   ├── api_preview.png            # FastAPI documentation
│   ├── architecture.png           # System architecture diagram
│   ├── results_summary.png        # Model performance and insights
│   └── feature_analysis.png       # Feature importance and correlations
│
├── demo/                 # Demo video resources and guides
│   └── DEMO_GUIDE.md             # Instructions for creating demo videos
│
└── generate_screenshots.py        # Script to regenerate screenshots

```

## 🎨 Screenshots

All screenshots are generated programmatically using matplotlib and seaborn to ensure consistency and reproducibility.

### Generation

To regenerate all screenshots:

```bash
python assets/generate_screenshots.py
```

Requirements:
- matplotlib
- seaborn
- pandas
- numpy

### Specifications

- **Format:** PNG
- **Resolution:** 150 DPI
- **Color:** Full color with white background
- **Size:** Optimized for web and print

## 📸 Screenshot Descriptions

### 1. dashboard_preview.png
**Dimensions:** ~1600x1200px  
**Content:** 
- Project metrics overview
- Feature importance chart
- Model comparison bars
- Popularity distribution histogram

### 2. api_preview.png
**Dimensions:** ~1400x1000px  
**Content:**
- FastAPI endpoint list with HTTP methods
- Example request/response format
- Interactive documentation link

### 3. architecture.png
**Dimensions:** ~1400x1000px  
**Content:**
- System architecture layers
- Component interactions
- Data flow visualization

### 4. results_summary.png
**Dimensions:** ~1400x1000px  
**Content:**
- Model MAE and R² comparisons
- Feature importance distribution
- Key insights summary

### 5. feature_analysis.png
**Dimensions:** ~1400x1000px  
**Content:**
- Scatter plots of feature relationships
- Correlation heatmap
- Distribution comparisons

## 🎥 Demo Resources

See `demo/DEMO_GUIDE.md` for comprehensive instructions on:
- Creating demo videos
- Recording screen captures
- Making animated GIFs
- Publishing demos

## 📝 Usage Guidelines

### In Documentation
```markdown
![Dashboard Preview](assets/screenshots/dashboard_preview.png)
```

### In Presentations
- All images are high-resolution and suitable for presentations
- Use with proper attribution to the project

### In Academic Reports
- Screenshots demonstrate the practical implementation
- Can be included in methodology and results sections

## 🔄 Updating Assets

When updating the project:

1. **Visual Changes:** If the UI changes, regenerate screenshots
2. **New Features:** Add new screenshots showcasing them
3. **Consistency:** Keep visual style consistent across all assets
4. **Documentation:** Update this README with new asset descriptions

## 📄 License

All visual assets in this directory are part of the Spotify Analysis project and are licensed under the MIT License, consistent with the project license.

## 🙏 Credits

Screenshots generated using:
- **matplotlib** - Plotting library
- **seaborn** - Statistical visualization
- **Python** - Automation and scripting

---

*Last updated: December 2025*
