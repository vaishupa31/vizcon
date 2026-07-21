import streamlit as st
import pandas as pd
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
st.write("Looking for data in:", DATA_DIR)
st.write("Files there:", os.listdir(DATA_DIR) if os.path.exists(DATA_DIR) else "FOLDER DOES NOT EXIST")


@st.cache_data
def load_metrics():
    """Year-level summary with countryness (268K rows)."""
    df = pd.read_csv(os.path.join(DATA_DIR, "metrics-and-summary.csv"))
    df = df[df["year"] >= 1997]  # Only 1997+ (all 8 countries)
    return df


@st.cache_data
def load_summary():
    """Aggregated 1997-2023 summary (19K rows)."""
    return pd.read_csv(os.path.join(DATA_DIR, "summary-1997-2023.csv"))


@st.cache_data
def load_all_names():
    """Full granular data (1.55M rows) — use sparingly!"""
    df = pd.read_csv(os.path.join(DATA_DIR, "all-names-long.csv"))
    df = df[df["year"] >= 1997]
    return df
