from models.prepare_data import load_and_clean_data
from models.train_linear_model import train_and_save_model

def main():
    print("Loading data...")
    df = load_and_clean_data()
    print("Data loaded. Training model...")

    model, mse, r2 = train_and_save_model(df)

    print("Training complete.")
    print(f"  MSE: {mse:,.2f}")
    print(f"  R² Score: {r2:.4f}")

if __name__ == "__main__":
    main()