# Fake News Detection App

This is a **Flask web application** that predicts whether a piece of news is **REAL** or **FAKE** using a trained machine learning model.

---

## Features
- Input **news title** and **news content** via a simple web form.
- Text preprocessing (cleaning & lowercasing).
- Vectorization using **TF-IDF**.
- Prediction using a **Decision Tree Classifier**.
- Returns either:
  - ✅ REAL NEWS
  - ❌ FAKE NEWS

---

## Tech Stack
- **Python** (Flask, scikit-learn, joblib, numpy, re)
- **Machine Learning** (Decision Tree Classifier)
- **Frontend**: HTML (with Flask templates)
- **Model Files**: `tree_model.pkl`, `tree_vectorizer.pkl`

---

## Project Structure
📦 Decision_Tree
┣ 📜 app.py # Flask app
┣ 📜 tree_model.pkl # Trained decision tree model
┣ 📜 tree_vectorizer.pkl # TF-IDF vectorizer
┣ 📜 templates
┃ ┗ 📜 index.html # Frontend form
┗ 📜 decision_tree.ipynb

---

## How to Run Locally
1. Clone this repository:
   ```bash
   git clone https://github.com/Soniaify/fake-news-detection.git
   cd fake-news-detection
Install dependencies:
  - pip install flask scikit-learn joblib numpy
Make sure tree_model.pkl and tree_vectorizer.pkl are in the project folder.
Run the Flask app:
  - python app.py
Open your browser and go to:
  - http://127.0.0.1:5000/

## Future Improvements
  - Improve accuracy with advanced models (Logistic Regression, Random Forest, or Transformers).
  - Add a user-friendly UI with Bootstrap/TailwindCSS.
  - Deploy the app online (Heroku, Vercel, or AWS).

## Author
Developed by Sonia.
Feel free to fork, improve, and contribute!
