import joblib
import json
import numpy as np

try:
    model = joblib.load("burnout_model5.pkl")
    scaler = joblib.load("scaler5.pkl")

    # Extract Logistic Regression parameters
    # Equation: z = intercept + sum(coef * x)
    # prob = 1 / (1 + exp(-z))
    
    weights = model.coef_[0].tolist()
    intercept = model.intercept_[0].tolist()
    
    # Extract Scaler parameters (assuming StandardScaler)
    # scaled_x = (x - mean) / scale
    
    mean = scaler.mean_.tolist()
    scale = scaler.scale_.tolist()
    
    model_data = {
        "weights": weights,
        "intercept": intercept,
        "mean": mean,
        "scale": scale,
        "features": ['Age', 'Experience', 'WorkHoursPerWeek', 'RemoteRatio',
                     'SatisfactionLevel', 'StressLevel', 'Gender_Male',
                     'JobRole_Engineer', 'JobRole_HR', 'JobRole_Manager', 'JobRole_Sales']
    }
    
    with open("model_params.json", "w") as f:
        json.dump(model_data, f, indent=4)
        
    print("SUCCESS: Parameters extracted to model_params.json")

except Exception as e:
    print(f"ERROR: {str(e)}")
