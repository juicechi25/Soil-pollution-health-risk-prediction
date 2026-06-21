import pandas as pd
import joblib

# Load pre-trained models and encoders
scaler = joblib.load("scaler.pkl")
label_encoder = joblib.load("label_encoder.pkl")
columns = joblib.load("X_encoded_columns.pkl")
stack_model = joblib.load("stack_model.pkl")  # Make sure this was trained with `columns`

def preprocess_input(input_data):
    df = pd.DataFrame([input_data])
    df_encoded = pd.get_dummies(df)

    # Align input columns with training columns
    df_encoded = df_encoded.reindex(columns=columns, fill_value=0)

    return scaler.transform(df_encoded)

def predict_risk(X):
    # Predict probabilities with the stacking model
    stack_probs = stack_model.predict_proba(X)[0]
    diseases = label_encoder.classes_

    # Map class probabilities to disease names
    avg_risk = {d: p for d, p in zip(diseases, stack_probs)}
    avg_risk_percent = {d: round(p * 100, 1) for d, p in avg_risk.items()}

    # Get the most likely disease prediction
    most_likely = max(avg_risk.items(), key=lambda x: x[1])

    return most_likely[0], round(most_likely[1] * 100, 1), avg_risk_percent

def pad_input_data(user_input):
    """Fill missing fields with safe default values for consistent input structure."""
    base = {
        "Region": "Sydney",
        "Pollutant_Type": "Arsenic",
        "Pollutant_Concentration_mg_kg": 32.0,
        "Soil_pH": 6.5,
        "Temperature_C": 25,
        "Humidity_%": 60,
        "Rainfall_mm": 100.0,
        "Crop_Type": "Corn",
        "Farming_Practice": "Conventional",
        "Mitigation_Measure": "Chemical Neutralization",
        "Nearby_Industry": "Agriculture",
        "Water_Source_Type": "River",
        "Soil_Texture": "Clay"
    }

    base.update(user_input)
    return base

def handle_prediction_request(raw_data):
    print("📦 Received input:", raw_data)

    user_input = {
        "Region": raw_data.get("region", "Sydney"),
        "Pollutant_Type": raw_data.get("pollutant_type", "Lead"),
        "Pollutant_Concentration_mg_kg": 32.0,
        "Soil_pH": 6.7,
        "Temperature_C": 27,
        "Humidity_%": 50,
        "Rainfall_mm": 100.0,
        "Crop_Type": raw_data.get("crop_type", "Wheat"),
        "Farming_Practice": raw_data.get("farming_practice", "Conventional"),
        "Mitigation_Measure": raw_data.get("mitigation_measure", "None"),
        "Nearby_Industry": raw_data.get("nearby_industry", "Chemical"),
        "Water_Source_Type": raw_data.get("water_source_type", "River"),
        "Soil_Texture": raw_data.get("soil_texture", "Clay")
    }

    # Pad with defaults
    user_input = pad_input_data(user_input)
    print("🧪 Input to model:", user_input)

    # Preprocess and predict
    X = preprocess_input(user_input)
    disease, confidence, distribution = predict_risk(X)

    # Build response
    return {
        "prediction": disease,
        "confidence": confidence,
        "distribution": distribution
    }
