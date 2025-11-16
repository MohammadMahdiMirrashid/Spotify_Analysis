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

## Quickstart

1. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate  # macOS / Linux
.venv\Scripts\activate     # Windows (PowerShell)
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Place your dataset CSV in `data/raw/` and run the first notebook (`01_data_exploration.ipynb`) to create a cleaned CSV in `data/`.

---

## Notebooks

* `01_data_exploration.ipynb` — load data, clean, basic summaries, save cleaned dataframe.
* `02_feature_analysis.ipynb` — EDA, visualizations, correlation matrices, genre comparisons.
* `03_modeling.ipynb` — prepare features, train classification models to predict popularity category, evaluate results.

---

## Model target

Create a categorical target for popularity:

* 0 = Low (<40)
* 1 = Medium (40–60)
* 2 = High (>60)

Recommended features: `energy, valence, acousticness, danceability, instrumentalness, loudness, tempo`.

---

## Contributing

* Add your dataset to `data/raw/` (keep raw untouched once imported).
* Write modular functions into `src/` and import them into notebooks.

---

## License

Choose a license for your repo (e.g., MIT) and add a `LICENSE` file.


