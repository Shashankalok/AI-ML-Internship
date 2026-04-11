import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib
import os
import json

print(" Training started...")

# Load data
df = pd.read_csv('Housing.csv')

# Encode categorical variables
categorical_columns = [
    'mainroad', 'guestroom', 'basement',
    'hotwaterheating', 'airconditioning',
    'prefarea', 'furnishingstatus'
]

label_encoders = {}

for column in categorical_columns:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le

# Save encoders
joblib.dump(label_encoders, 'label_encoders.joblib')

# Features & target
X = df.drop('price', axis=1)
y = df['price']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Save scaler
joblib.dump(scaler, 'scaler.joblib')

# Model
model = RandomForestRegressor(
    n_estimators=50,
    max_depth=10,
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=42,
    n_jobs=-1
)

# Train
model.fit(X_train_scaled, y_train)

# Predictions
y_pred_train = model.predict(X_train_scaled)
y_pred_test = model.predict(X_test_scaled)

# Metrics
train_r2 = model.score(X_train_scaled, y_train)
test_r2 = model.score(X_test_scaled, y_test)

mae = mean_absolute_error(y_test, y_pred_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred_test))

print(f" Train R²: {train_r2:.4f}")
print(f" Test R²: {test_r2:.4f}")
print(f" MAE: {mae:.2f}")
print(f" RMSE: {rmse:.2f}")

# Save model
joblib.dump(model, 'house_price_model.joblib')

# Save metrics ( important for next step)
model_info = {
    "train_r2": float(train_r2),
    "test_r2": float(test_r2),
    "mae": float(mae),
    "rmse": float(rmse)
}

with open('model_info.json', 'w') as f:
    json.dump(model_info, f)

print("📁 Model & metrics saved successfully!")

# File sizes
for file in ['house_price_model.joblib', 'scaler.joblib', 'label_encoders.joblib']:
    size = os.path.getsize(file) / (1024 * 1024)
    print(f"{file}: {size:.2f} MB")

print("🎉 Training complete!")