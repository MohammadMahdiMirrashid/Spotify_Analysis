"""Simple plotting helpers using matplotlib.
Keep plotting functions small so notebooks remain readable.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

FIG_DIR = Path('reports/figures')
FIG_DIR.mkdir(parents=True, exist_ok=True)


def save_hist(series: pd.Series, filename: str, bins: int = 30):
    """Save a histogram plot."""
    plt.figure()
    series.hist(bins=bins)
    plt.xlabel(series.name)
    plt.tight_layout()
    plt.savefig(FIG_DIR / filename)
    plt.close()


def save_corr_heatmap(df: pd.DataFrame, cols: list, filename: str):
    """Save a correlation heatmap."""
    plt.figure()
    corr = df[cols].corr()
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', center=0, square=True)
    plt.title('Correlation matrix')
    plt.tight_layout()
    plt.savefig(FIG_DIR / filename)
    plt.close()

