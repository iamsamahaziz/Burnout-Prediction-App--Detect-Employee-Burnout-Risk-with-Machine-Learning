from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("burnout_model5.pkl")
scaler = joblib.load("scaler5.pkl")

model_columns = ['Age', 'Experience', 'WorkHoursPerWeek', 'RemoteRatio', 
                 'SatisfactionLevel', 'StressLevel', 'Gender_Male', 
                 'JobRole_Engineer', 'JobRole_HR', 'JobRole_Manager', 'JobRole_Sales']

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    age = int(request.form["age"])
    experience = int(request.form["experience"])
    work_hours = int(request.form["work_hours"])
    remote_ratio = int(request.form["remote_ratio"])
    satisfaction = float(request.form["satisfaction"])
    stress = int(request.form["stress"])
    gender = request.form["gender"]
    job_role = request.form["job_role"]

    df = pd.DataFrame([{
        "Age": age,
        "Experience": experience,
        "WorkHoursPerWeek": work_hours,
        "RemoteRatio": remote_ratio,
        "SatisfactionLevel": satisfaction,
        "StressLevel": stress,
        "Gender": gender,
        "JobRole": job_role
    }])


    df = pd.get_dummies(df, columns=["Gender", "JobRole"], drop_first=True)

    df = df.reindex(columns=model_columns, fill_value=0)

    features_scaled = scaler.transform(df)
    ml_probability = model.predict_proba(features_scaled)[0][1] * 100

    rule_score = 0
    
    if stress >= 8:
        rule_score += 50
    elif stress >= 6:
        rule_score += 35
    elif stress >= 4:
        rule_score += 15
    
    if work_hours >= 60:
        rule_score += 40
    elif work_hours >= 50:
        rule_score += 25
    elif work_hours >= 45:
        rule_score += 10
    
    if satisfaction <= 1.5:
        rule_score += 35
    elif satisfaction <= 2.5:
        rule_score += 20
    elif satisfaction <= 3.0:
        rule_score += 10
    
    if remote_ratio < 20 and stress >= 5:
        rule_score += 15

    probability = (ml_probability * 0.3) + (rule_score * 0.7)
    probability = min(probability, 100)


    if probability < 20:
        result = "✅ Risque faible de Burnout"
    elif probability < 45:
        result = "⚠️ Risque modéré de Burnout"
    elif probability < 70:
        result = "🔴 Risque élevé de Burnout"
    else:
        result = "🚨 Risque très élevé de Burnout"

    return render_template("index.html", result=result, probability=round(probability, 1))

if __name__ == "__main__":
    app.run()
