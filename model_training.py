import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load dataset
data = pd.read_csv("house_prices.csv")

# Drop irrelevant columns
columns_to_drop = ['Id', 'Alley', 'PoolQC', 'Fence', 'MiscFeature']
data = data.drop(columns=columns_to_drop, axis=1)

# Convert categorical variables
data = pd.get_dummies(data, drop_first=True)

# Handle missing values
data = data.fillna(data.median())

# Split features and target
X = data.drop('SalePrice', axis=1)
y = data['SalePrice']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Random Forest model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)
model.fit(X_train, y_train)

# Save model and feature names
with open("model.pkl", "wb") as f:
    pickle.dump((model, X.columns), f)

print("✅ Model trained and saved as model.pkl")
