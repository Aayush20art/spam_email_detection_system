# 🛡️ SpamShield — Email Spam Detector

> **AI-powered email spam detection web app built with Streamlit & Scikit-learn**
---

## 📌 Overview

**SpamShield** is a machine learning web application that detects whether an email is **spam or legitimate (ham)** in real time. It uses a trained **Multinomial Naive Bayes** classifier with **TF-IDF vectorization** and presents results through a sleek Deep Space–themed Streamlit UI.

---

## ✨ Features

- 🤖 **ML-Powered** — Multinomial Naive Bayes classifier
- 📊 **99% Accuracy** — Trained on ~5,500 real-world emails
- ⚡ **Instant Results** — Real-time prediction with confidence score
- 🎨 **Custom UI** — Deep Space dark theme with purple/indigo neon aesthetics
- 🔐 **Confidence Score** — Shows prediction probability alongside result

---

## 🖥️ Demo

```
Input  → "Congratulations! You've won a FREE iPhone. Click here to claim now!"
Output → 🚨 SPAM DETECTED — Confidence 97.3%

Input  → "Hey, are we still meeting tomorrow at 3pm?"
Output → ✅ CLEAN EMAIL — Confidence 99.1%
```

---

## 🗂️ Project Structure

```
SpamShield/
│
├── spam_detector_app.py   # Main Streamlit app
├── MultinomialNB.pkl      # Trained Naive Bayes model
├── vectorizer.pkl         # Fitted TF-IDF vectorizer
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run spam_detector_app.py
```

The app will open at `http://localhost:8501`

---

## 📦 Requirements

```txt
streamlit
scikit-learn
joblib
numpy
```

> Create a `requirements.txt` using:
> ```bash
> pip freeze > requirements.txt
> ```

---

## 🧠 How It Works

```
Email Text Input
      ↓
TF-IDF Vectorization  (converts text → numerical features)
      ↓
Multinomial Naive Bayes Classifier
      ↓
Prediction → SPAM (1) or HAM (0)  +  Confidence %
```

| Step | Description |
|------|-------------|
| 🧹 Preprocessing | Tokenization, stopword removal |
| 🔢 Feature Extraction | TF-IDF Bag-of-Words representation |
| 🤖 Classification | Naive Bayes probabilistic prediction |
| 📊 Output | Spam/Ham label + confidence percentage |

---

## 📈 Model Performance

| Metric | Score |
|--------|-------|
| Accuracy | **99%** |
| Algorithm | Multinomial Naive Bayes |
| Training Data | ~5,500 emails |
| Vectorizer | TF-IDF |

---

## 🎨 UI Theme

- **Background** — Deep Space (`#07071a`) with radial purple/indigo glows
- **Typography** — `Space Mono` (headings) + `DM Sans` (body)
- **Accents** — Purple `#6d28d9` · Indigo `#4f46e5` · Violet `#7c3aed`
- **Effects** — Floating icon animation, neon button glow on hover, dot-grid overlay

---

## 👤 Author

**Aayush Sharma**
- 🎓 B.Tech Information Technology — Chandigarh Engineering College, Landran (2026)
- 💼 Aspiring Data Analyst & ML Engineer
- 🔗 [LinkedIn](www.linkedin.com/in/aayush-sharma-b108a93b0)

---

<div align="center">
  <sub>🛡️ SpamShield · Built with ♥ by Aayush Sharma · Streamlit × Scikit-learn</sub>
</div>
