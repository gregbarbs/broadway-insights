import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from models.prepare_data import load_and_clean_data
from models.train_linear_model import train_and_save_model
from sklearn.model_selection import train_test_split

# Ensure save directory exists
output_dir = "backend/static"
os.makedirs(output_dir, exist_ok=True)

def generate_visualizations():
    df = load_and_clean_data()
    X = df[["WeeklyAttendance", "CapacityFilled", "GrossPotential", "NumPerformances"]]
    y = df["Gross"]

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Train model
    model, _, _ = train_and_save_model(df)
    predictions = model.predict(X_test)

    # 1. Scatter Plot: Predicted vs. Actual Gross
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=y_test, y=predictions, alpha=0.6)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--r')
    plt.xlabel("Actual Gross ($)")
    plt.ylabel("Predicted Gross ($)")
    plt.title("Predicted vs. Actual Gross Revenue")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "predictions_vs_actuals.png"))
    plt.close()

    # 2. Boxplot: Gross Revenue by Show Type
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x="ShowType", y="Gross")
    plt.title("Gross Revenue Distribution by Show Type")
    plt.xlabel("Show Type")
    plt.ylabel("Gross ($)")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "gross_by_showtype.png"))
    plt.close()

    # 3. Scatter Plot: Weekly Attendance vs. Gross
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x="WeeklyAttendance", y="Gross", hue="ShowType", alpha=0.6)
    plt.title("Attendance vs. Gross Revenue")
    plt.xlabel("Weekly Attendance")
    plt.ylabel("Gross ($)")
    plt.tight_layout()
    plt.legend(title="Show Type", loc="best")
    plt.savefig(os.path.join(output_dir, "attendance_vs_gross.png"))
    plt.close()

    print(f"Visualizations saved to '{output_dir}'")

if __name__ == "__main__":
    generate_visualizations()
