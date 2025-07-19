from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import joblib
import pandas as pd
import os
import logging
from datetime import datetime
import datetime

app = Flask(__name__)
CORS(app, origins=["http://localhost:63342"])

# Load model and R² score on startup
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MODEL_PATH = os.path.join(PROJECT_ROOT, "models", "saved", "linear_regression_model.pkl")

# Load bundled model and metadata (a dictionary with 'model', 'r2_score', and 'residual_std')
model_bundle = joblib.load(MODEL_PATH)
model = model_bundle["model"]
r2_score_val = model_bundle["r2_score"]
residual_std = model_bundle["residual_std"]

# Configure logging
logging.basicConfig(
    filename='logs.txt',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
)

@app.route('/')
def index():
    return send_from_directory("../frontend", "index.html")

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "OK", "message": "API is running"}), 200

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Parse and sanitize input
        input_df = pd.DataFrame([{
            "WeeklyAttendance": float(data["attendance"]),
            "CapacityFilled": float(data["capacity"]),
            "GrossPotential": float(data["potential"]),
            "NumPerformances": float(data["shows"])
        }])

        prediction = model.predict(input_df)[0]

        # Confidence interval (95%)
        margin = 1.96 * residual_std
        lower = round(prediction - margin, 2)
        upper = round(prediction + margin, 2)

        # Log the successful request
        logging.info(f"Prediction request: {data} | Prediction: {round(prediction, 2)}")

        os.makedirs("backend/logs", exist_ok=True)

        # Log the prediction with timestamp
        with open("backend/logs/predictions.log", "a") as f:
            f.write(f"{datetime.datetime.now()} - Input: {data} => "
                    f"Predicted Gross: ${prediction:.2f} (R²: {r2_score_val:.2%})\n")

        return jsonify({
            "estimated_gross": round(prediction, 2),
            "confidence_low": lower,
            "confidence_high": upper,
            "r2_score": f"{r2_score_val * 100:.2f}%"
        })

    except Exception as e:
        # Log any failure
        logging.error(f"Prediction failed: {e} | Data: {request.get_json()}")
        return jsonify({"error": str(e)}), 400

@app.route("/visuals")
def show_visuals():
    return send_from_directory("../frontend", "visuals.html")

if __name__ == "__main__":
    app.run(debug=True)