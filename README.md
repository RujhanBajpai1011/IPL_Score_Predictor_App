# 🏏 IPL Score Predictor App

This is a Streamlit-based web application that predicts the final score of an ongoing IPL match using a trained machine learning model.

## 🔮 Features

- Predicts first innings final score based on:
  - Batting and bowling teams
  - Overs completed
  - Current runs and wickets
  - Last 5 overs performance
- Intuitive and clean UI built with Streamlit
- Uses a `RandomForestRegressor` or similar model trained on past IPL data

## 🛠️ Tech Stack

- Python
- Streamlit
- scikit-learn
- NumPy
- pickle (for loading the ML model)

## 🚀 How to Run Locally

1. Clone this repo
2. Place your trained model file as `ml_model.pkl` in the same directory
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
