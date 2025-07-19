import pandas as pd

def load_and_clean_data(csv_path="data/broadway-weekly-grosses.csv"):
    df = pd.read_csv(csv_path)

    # Convert FullDate to datetime
    df["FullDate"] = pd.to_datetime(df["FullDate"], format="%m/%d/%y", errors="coerce")

    # Clean numeric columns: remove commas and percent signs, then convert to numeric
    df["WeeklyAttendance"] = pd.to_numeric(df["WeeklyAttendance"].str.replace(",", ""), errors="coerce")
    df["Gross"] = pd.to_numeric(df["Gross"].str.replace(",", ""), errors="coerce")
    df["CapacityFilled"] = pd.to_numeric(df["CapacityFilled"].str.replace("%", ""), errors="coerce")
    df["GrossPotential"] = pd.to_numeric(df["GrossPotential"].str.replace("%", ""), errors="coerce")

    # Ensure NumPerformances is numeric
    df["NumPerformances"] = pd.to_numeric(df["NumPerformances"], errors="coerce")

    # Drop rows with missing or malformed data
    df = df.dropna()

    return df