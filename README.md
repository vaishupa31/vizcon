# 🧬 The DNA of a Name — VizCon 2026

> Same Language. Different Cultures. What 200 million baby names reveal about the invisible borders between 8 English-speaking nations.

## 🚀 Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 📁 Structure

```
streamlit-app/
├── app.py                 # Main entry point + sidebar navigation
├── pages/
│   ├── __init__.py
│   ├── home.py            # 🏠 Overview: Anglosphere + Two Truths
│   ├── lifespan.py        # ⏳ Half-life, lifecycles, zombies
│   ├── contagion.py       # 🦠 Spread speed, cultural highways
│   ├── borders.py         # 🪞 Pronunciation wall (key page)
│   └── convergence.py     # 🌊 Paradox, import/export, fun facts
├── data/                  # Processed JSON/CSV for charts
├── .streamlit/
│   └── config.toml        # Dark theme config
├── requirements.txt
└── README.md
```

## 📊 Data Source

Anglosphere Baby Names Dataset (Kaggle) — 1.55M records, 8 countries, 1935–2023.

## 🤖 GenAI Usage

AI-assisted data exploration, pattern discovery, code generation, and narrative drafting.
See Methodology page in the app for full documentation.
