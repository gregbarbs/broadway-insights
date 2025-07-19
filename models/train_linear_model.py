import os
import joblib
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from models.prepare_data import load_and_clean_data

def train_and_save_model(df=None):
    if df is None:
        df = load_and_clean_data()

    print("Loading data...")
    df = load_and_clean_data()
    print("Data loaded. Training model...")

    # Select features and target
    X = df[["WeeklyAttendance", "CapacityFilled", "GrossPotential", "NumPerformances"]]
    y = df["Gross"]

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    # Standard deviation of residuals
    residuals = y_test - predictions
    std_error = np.std(residuals)

    # Evaluate
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    print(f"Training complete.\n  MSE: {mse:,.2f}\n  R² Score: {r2:.4f}")

    # Save model and R²
    os.makedirs("models/saved", exist_ok=True)
    save_path = os.path.join("models", "saved", "linear_regression_model.pkl")
    joblib.dump({
        "model": model,
        "r2_score": r2,
        "residual_std": std_error
    }, save_path)
    print(f"Model saved to {save_path}")
    return model, r2, std_error

if __name__ == "__main__":
    train_and_save_model()
