import streamlit as st
from pp import predict_price

st.set_page_config(page_title="House Price Predictor", layout="centered")

st.title("🏠 House Price Prediction App")
st.write("Enter house features to predict the sale price.")

# User inputs
overall_qual = st.slider("Overall Quality (1–10)", 1, 10, 5)
gr_liv_area = st.number_input("Above Ground Living Area (sq ft)", 500, 5000, 1500)
garage_cars = st.slider("Garage Capacity (Cars)", 0, 4, 2)
total_bsmt_sf = st.number_input("Total Basement Area (sq ft)", 0, 3000, 800)
year_built = st.number_input("Year Built", 1900, 2024, 2005)

# Input dictionary (must match training features)
input_data = {
    "OverallQual": overall_qual,
    "GrLivArea": gr_liv_area,
    "GarageCars": garage_cars,
    "TotalBsmtSF": total_bsmt_sf,
    "YearBuilt": year_built
}

if st.button("Predict House Price"):
    price = predict_price(input_data)
    st.success(f"💰 Estimated House Price: ${price}")
