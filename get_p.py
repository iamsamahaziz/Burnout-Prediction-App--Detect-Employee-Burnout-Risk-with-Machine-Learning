import joblib, json, numpy as np
try:
    m = joblib.load('burnout_model5.pkl')
    s = joblib.load('scaler5.pkl')
    # Get first calibrated classifier's base estimator
    base = m.calibrated_classifiers_[0].base_estimator
    d = {
        'w': base.coef_[0].tolist(),
        'i': base.intercept_[0].tolist(),
        'm': s.mean_.tolist(),
        's': s.scale_.tolist()
    }
    with open('p.json', 'w') as f:
        json.dump(d, f)
    print('SUCCESS')
except Exception as e:
    print('ERROR:', e)
