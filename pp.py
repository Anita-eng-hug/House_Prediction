import pickle
import pandas as pd

# Load trained model
with open("model.pkl", "rb") as f:
    model, feature_names = pickle.load(f)

def predict_price(input_data: dict):
    """
    input_data: dictionary of feature values
    """
    input_df = pd.DataFrame([input_data])

    # Ensure all columns exist
    for col in feature_names:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[feature_names]

    prediction = model.predict(input_df)[0]
    return round(prediction, 2)
