# 🔥 BurnoutGuard AI - Advanced Wellness Dashboard

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.2-green.svg)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.8.0-orange.svg)](https://scikit-learn.org/)
[![PWA](https://img.shields.io/badge/PWA-Ready-blueviolet.svg)](https://web.dev/progressive-web-apps/)
[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen.svg)](http://Solvex.pythonanywhere.com)

**BurnoutGuard AI** is an advanced professional wellness dashboard that leverages **Machine Learning** to help users detect, track, and manage workplace stress. Designed with a premium glassmorphic UI, it combines scientific analysis with immediate mental health tools.

![App Preview](Preview.png)

## 🚀 Key Features

### 🧠 Pure Machine Learning Assessment
- **Logistic Regression Engine**: 100% model-driven predictions powered by a `burnout_model5.pkl` trained on real professional data.
- **Factor Breakdown**: Visualized impact analysis of Stress Level, Work Hours, Job Satisfaction, and Remote Work ratio.
- **Dynamic Recommendations**: Personalized wellness tips generated based on your specific risk profile.
- **30-Day Action Plan**: A tailored, 4-week wellness roadmap to improve mental health and productivity.

### 🌟 Advanced Integrated Tools
- **📊 Industry Comparison**: Benchmark your risk score against role-specific averages for Engineers, Managers, Analysts, HR, and Sales professionals.
- **✨ Breathing Exercise**: Built-in guided **4-7-8 breathing module** with pulsing animations for immediate workplace stress relief.
- **😊 Daily Mood Tracker**: Interactive 30-day mood heatmap with streak tracking and personal journaling.
- **📄 Professional Reports**: Export a high-quality PDF report including your risk profile, factor analysis, and action plan.

### 🆕 Latest Features
- **⭐ Star Rating Feedback**: Users can rate their experience (1-5 stars) with optional comments. All feedback is saved server-side.
- **🏆 Wellness Badges**: Gamified achievement system — unlock 6 badges (First Step, Low Risk Hero, Improving, 7-Day Streak, Action Taker, Mindful).
- **� Score History Chart**: Server-side tracking with a Chart.js line chart showing your last 10 assessments and a trend arrow (↑ Improving / ↓ Worsening / → Stable).
- **🎉 Confetti Celebration**: Score below 20%? You get a fun confetti animation to celebrate your healthy balance!
- **🔄 Color-Coded Progress Ring**: The gauge ring changes color based on severity — green (<20%), yellow (<45%), orange (<70%), red (≥70%).
- **📋 Feedback Dashboard**: View all user ratings and comments at `/view-feedback`.

### 🛠️ Technical Excellence
- **Tech Stack**: Python (Flask), Scikit-Learn (Logistic Regression), Pandas, Joblib.
- **Frontend**: Vanilla JavaScript (ES6+), CSS3 (Glassmorphism), Chart.js (Radar & Trend charts), canvas-confetti.
- **Architecture**: Lightweight, comment-free production code optimized for performance.
- **Mobile First**: Fully responsive PWA (Progressive Web App) with offline caching support via Service Workers.

## 🔧 Setup & Installation

1. **Clone & Install:**
   ```bash
   git clone https://github.com/iamsamahaziz/burnout-prediction-app.git
   cd burnout-prediction-app
   pip install -r requirements.txt
   ```

2. **Run Locally:**
   ```bash
   python app.py
   ```
   Access the dashboard at `http://localhost:5000`.

## ☁️ Live Demo & Deployment

- **🌐 Live App**: [http://Solvex.pythonanywhere.com](http://Solvex.pythonanywhere.com)
- **📋 Feedback Dashboard**: [http://Solvex.pythonanywhere.com/view-feedback](http://Solvex.pythonanywhere.com/view-feedback)
- Configured for professional hosting on **PythonAnywhere**, **Microsoft Azure**, and **Google Cloud App Engine**.

---
Created by **Samah AZIZ** · Empowering professional well-being through Data Science.
