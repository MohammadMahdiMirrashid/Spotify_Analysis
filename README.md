# Spotify Songs Analysis: Audio Features, Trends & Popularity Prediction

## Overview
This project performs an end-to-end analysis of the **Spotify Songs Dataset**, exploring audio features, genre patterns, correlations, and building a machine learning model to predict a song's popularity category based on its characteristics.

It is designed as a portfolio-ready data project that demonstrates:
- Data cleaning and preprocessing
- SQL-style querying within Python
- Exploratory Data Analysis (EDA)
- Visualizations
- Feature correlations
- Predictive modeling (classification)
- Clear, documented workflow

---

## Repository Structure

```
spotify-songs-analysis/
├── README.md
├── requirements.txt
├── data/
│   ├── raw/ (put original CSVs here)
│   └── clean_spotify.csv
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_feature_analysis.ipynb
│   └── 03_modeling.ipynb
├── src/
│   ├── __init__.py
│   ├── data_processing.py
│   ├── visualization.py
│   └── modeling.py
├── reports/
│   └── figures/
└── models/
```

---

## Dataset Instructions

### 1. Download the dataset
Use the Kaggle dataset **Spotify Tracks Dataset**:
- Go to Kaggle and search for **"Spotify Tracks Dataset"** (typically published by *Mélanie B.* or *Josu Gómez* depending on version).
- Download the main CSV file. Common filenames include:
  - `SpotifyFeatures.csv`
  - `tracks.csv`
  - `data.csv`

Any of these versions will work as long as the following columns exist or have equivalents:
- `danceability`
- `energy`
- `loudness`
- `acousticness`
- `instrumentalness`
- `liveness`
- `valence`
- `tempo`
- `duration_ms`
- `popularity`
- `genre` or `playlist_genre`

### 2. Place the dataset in your repository
Put the downloaded CSV into:
```
data/raw/
```
Example:
```
data/raw/SpotifyFeatures.csv
```

### 3. Update the notebook to point to the correct filename
In `01_data_exploration.ipynb`, the code will automatically try multiple filenames, or you can modify:
```python
RAW_PATH = 'data/raw/SpotifyFeatures.csv'
```
(or whatever your file is named).

### 4. Data dictionary

Different versions of the dataset use slightly different labels. Here is the standardized meaning:

* **danceability** – how suitable a track is for dancing (0–1)
* **energy** – intensity and activity (0–1)
* **loudness** – average volume in dB (negative values)
* **acousticness** – probability the track is acoustic (0–1)
* **instrumentalness** – likelihood the track has no vocals (0–1)
* **liveness** – probability the track is live (0–1)
* **valence** – musical positivity (0–1)
* **tempo** – beats per minute
* **duration_ms** – track length in milliseconds
* **popularity** – Spotify popularity score (0–100)
* **genre / playlist_genre** – categorical label of track genre

---

## Requirements

This project requires Python 3.8 or higher. All dependencies are listed in `requirements.txt`:

### Core Dependencies
- **pandas** (≥1.5) - Data manipulation and analysis
- **numpy** (≥1.23) - Numerical computing
- **scikit-learn** (≥1.2) - Machine learning models and utilities
- **matplotlib** (≥3.6) - Basic plotting
- **seaborn** (≥0.12) - Statistical visualizations
- **joblib** (≥1.0) - Model serialization

### Development Dependencies
- **jupyterlab** (≥3.0) - Interactive notebook environment
- **ipython** (≥8.0) - Enhanced Python shell
- **notebook** (≥6.0) - Jupyter notebook support

### Optional Dependencies
- **xgboost** (≥1.7) - Gradient boosting (uncomment in requirements.txt if needed)

## Installation & Quickstart

1. **Clone or download this repository**

2. **Create and activate a virtual environment** (recommended):

```bash
python -m venv .venv
source .venv/bin/activate  # macOS / Linux
.venv\Scripts\activate     # Windows (PowerShell)
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

4. **Place your dataset CSV in `data/raw/`** and run the first notebook (`01_data_exploration.ipynb`) to create a cleaned CSV in `data/`.

5. **Launch Jupyter Lab** to start exploring:

```bash
jupyter lab
```

---

## Project Components

### Source Code (`src/`)

The project includes modular Python utilities:

- **`data_processing.py`** - Functions for loading, cleaning, and normalizing Spotify data
  - `load_raw()` - Load CSV files
  - `normalize_columns()` - Standardize column names
  - `basic_clean()` - Remove duplicates and filter invalid records
  - `save_clean()` - Export cleaned datasets

- **`visualization.py`** - Plotting helpers for analysis
  - `save_hist()` - Generate and save histograms
  - `save_corr_heatmap()` - Create correlation heatmaps

- **`modeling.py`** - Machine learning pipeline utilities
  - `make_baseline_model()` - Create baseline logistic regression pipeline
  - `train_and_evaluate()` - Train models and compute metrics
  - `save_model()` - Persist trained models to disk

### Notebooks (`notebooks/`)

* **`01_data_exploration.ipynb`** — Load data, clean, basic summaries, save cleaned dataframe
* **`02_feature_analysis.ipynb`** — EDA, visualizations, correlation matrices, genre comparisons
* **`03_modeling.ipynb`** — Prepare features, train classification models to predict popularity category, evaluate results

---

## Model target

Create a categorical target for popularity:

* 0 = Low (<40)
* 1 = Medium (40–60)
* 2 = High (>60)

Recommended features: `energy, valence, acousticness, danceability, instrumentalness, loudness, tempo`.

---

## Usage

### Running the Analysis

1. Start with `01_data_exploration.ipynb` to load and clean your dataset
2. Use `02_feature_analysis.ipynb` to explore patterns and relationships
3. Run `03_modeling.ipynb` to build and evaluate predictive models

### Using the Source Modules

Import the utilities in your notebooks or scripts:

```python
from src.data_processing import load_raw, basic_clean, save_clean
from src.visualization import save_hist, save_corr_heatmap
from src.modeling import make_baseline_model, train_and_evaluate, save_model
```

## Contributing

* Add your dataset to `data/raw/` (keep raw data untouched once imported)
* Write modular functions into `src/` and import them into notebooks
* Follow the existing code structure and documentation style

---
