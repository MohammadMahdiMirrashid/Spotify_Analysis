"""Basic data processing utilities for Spotify Songs Analysis."""
from pathlib import Path
from typing import Union
import pandas as pd
import numpy as np

DATA_DIR = Path('data')

def load_raw(csv_path: Union[str, Path]) -> pd.DataFrame:
    """Load raw CSV file."""
    df = pd.read_csv(csv_path)
    return df


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize column names to snake_case."""
    df = df.copy()
    df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]
    return df


def basic_clean(df: pd.DataFrame) -> pd.DataFrame:
    """Perform basic data cleaning operations."""
    df = df.copy()
    # drop duplicates
    df = df.drop_duplicates()
    # example filters
    if 'duration_ms' in df.columns:
        df = df[df['duration_ms'] > 1000]
    # enforce numeric where possible
    for col in df.columns:
        if df[col].dtype == object:
            try:
                df[col] = pd.to_numeric(df[col])
            except Exception:
                pass
    return df


def save_clean(df: pd.DataFrame, filename: str = 'clean_spotify.csv') -> None:
    """Save cleaned dataframe to CSV."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(DATA_DIR / filename, index=False)

