import argparse
import joblib
import pandas as pd

def predict_gross(attendance, capacity, potential, shows):
    # Load model
    model = joblib.load("../models/saved/linear_regression_model.pkl")

    # Wrap input as DataFrame
    input_data = pd.DataFrame([{
        "WeeklyAttendance": attendance,
        "CapacityFilled": capacity,
        "GrossPotential": potential,
        "NumPerformances": shows
    }])

    # Predict
    predicted_gross = model.predict(input_data)[0]
    return predicted_gross

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Predict weekly Broadway show gross.")
    parser.add_argument("--attendance", type=int, required=True, help="Weekly attendance")
    parser.add_argument("--capacity", type=float, required=True, help="Capacity filled (%)")
    parser.add_argument("--potential", type=float, required=True, help="Gross potential (%)")
    parser.add_argument("--shows", type=int, required=True, help="Number of performances")

    args = parser.parse_args()
    result = predict_gross(args.attendance, args.capacity, args.potential, args.shows)

    print(f"\nEstimated Gross Revenue: ${result:,.2f}")
