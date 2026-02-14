# 🔥 Employee Burnout Prediction - Web App

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge" />
</p>

> **Interactive web application** for predicting employee burnout risk based on professional data, combining a Machine Learning model (logistic regression) with a rule-based scoring system.

---

## 📸 Overview

The user fills out a form with their professional information, and the application instantly returns:
- The **risk level** (low ✅ / moderate ⚠️ / high 🔴 / very high 🚨)
- The **burnout probability** as a percentage

---

## 🎯 Features

| Feature | Description |
|---|---|
| 🧠 **ML Prediction** | Logistic regression model trained on synthetic HR data |
| 📏 **Business Rules** | Scoring system based on stress, hours, satisfaction & remote work |
| ⚖️ **Hybrid Score** | Weighted combination: 30% ML + 70% business rules |
| 🌐 **Web Interface** | Interactive form with instant results |
| 🎨 **Modern Design** | Clean UI with gradients, card shadows & responsive layout |

---

## 🛠️ Tech Stack

| Tool | Usage |
|---|---|
| **Python 3.12** | Core language |
| **Flask** | Web framework (backend + routing) |
| **Scikit-learn** | Model training & `StandardScaler` |
| **Pandas** | Data preprocessing & one-hot encoding |
| **Joblib** | Model serialization (`.pkl`) |
| **HTML / CSS** | Frontend interface |

---

## 📊 Dataset

- **Source**: [Kaggle — Synthetic HR Burnout Dataset](https://www.kaggle.com/datasets/ankam6010/synthetic-hr-burnout-dataset)
- **Target variable**: `Burnout` (0 = No burnout, 1 = Burnout)

### Input Features

| Feature | Type | Description |
|---|---|---|
| `Age` | Numeric | Employee age |
| `Experience` | Numeric | Years of experience |
| `WorkHoursPerWeek` | Numeric | Weekly working hours |
| `RemoteRatio` | Numeric | Remote work percentage (0–100) |
| `SatisfactionLevel` | Numeric | Job satisfaction level (1–5) |
| `StressLevel` | Numeric | Stress level (1–10) |
| `Gender` | Categorical | Gender (one-hot encoded) |
| `JobRole` | Categorical | Role: Analyst, Engineer, HR, Manager, Sales |

---

## ⚙️ ML Pipeline

```
CSV Data
   │
   ▼
Preprocessing (drop "Name", one-hot encoding)
   │
   ▼
Normalization (StandardScaler)
   │
   ▼
Stratified 80/20 split
   │
   ▼
Logistic Regression (class_weight="balanced")
   │
   ▼
Decision threshold at 0.80
   │
   ▼
Export model (.pkl) + scaler (.pkl)
```

---

## 📈 Model Performance

| Metric | Score |
|---|---|
| **Accuracy** | 96.25% |
| **Recall (Burnout)** | 88.46% |
| **Precision (Burnout)** | 65.71% |

---

## 🧮 Hybrid Scoring System

The final prediction combines two approaches:

```
Final Score = (ML × 0.30) + (Business Rules × 0.70)
```

### Business Rules

| Factor | Condition | Points |
|---|---|---|
| 🔴 Stress | ≥ 8 → +50 · ≥ 6 → +35 · ≥ 4 → +15 | 0–50 |
| ⏰ Hours/week | ≥ 60 → +40 · ≥ 50 → +25 · ≥ 45 → +10 | 0–40 |
| 😞 Satisfaction | ≤ 1.5 → +35 · ≤ 2.5 → +20 · ≤ 3.0 → +10 | 0–35 |
| 🏠 Remote work | < 20% AND stress ≥ 5 → +15 | 0–15 |

### Risk Interpretation

| Probability | Result |
|---|---|
| < 20% | ✅ Low risk |
| 20 – 44% | ⚠️ Moderate risk |
| 45 – 69% | 🔴 High risk |
| ≥ 70% | 🚨 Very high risk |

---

## 📁 Project Structure

```
Burnout_Detection/
├── app.py                  # Flask app (routes + prediction logic)
├── burnout_model5.pkl      # Serialized logistic regression model
├── scaler5.pkl             # Serialized StandardScaler
├── templates/
│   └── index.html          # User interface (form + result display)
├── static/
│   └── style.css           # CSS styles (responsive design)
└── README.md
```

---

## 🚀 Installation & Usage

### 1. Clone the repository

```bash
git clone https://github.com/iamsamahaziz/burnout-prediction-app.git
cd burnout-prediction-app
```

### 2. Install dependencies

```bash
pip install flask pandas scikit-learn joblib
```

### 3. Run the application

```bash
python app.py
```

### 4. Open in your browser

```
http://127.0.0.1:5000
```

---

## 👤 Author

**Samah AZIZ**  
Computer Science Engineering Student — FST Mohammedia

[![GitHub](https://img.shields.io/badge/GitHub-iamsamahaziz-181717?style=flat-square&logo=github)](https://github.com/iamsamahaziz)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-samah--az-0A66C2?style=flat-square&logo=linkedin)](https://linkedin.com/in/samah-az)

---

<p align="center">
  Made with ❤️ & Python
</p>
