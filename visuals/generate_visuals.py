import matplotlib.pyplot as plt
import seaborn as sns
from models.prepare_data import load_and_clean_data

def plot_gross_distribution(data):
    plt.figure(figsize=(8, 6))
    sns.histplot(data["Gross"], bins=30, kde=True)
    plt.title("Distribution of Weekly Gross Revenue")
    plt.xlabel("Gross ($)")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("visuals/gross_distribution.png")
    plt.close()

def plot_feature_correlation(data):
    plt.figure(figsize=(8, 6))
    corr = data[["WeeklyAttendance", "CapacityFilled", "GrossPotential", "NumPerformances", "Gross"]].corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Feature Correlation Matrix")
    plt.tight_layout()
    plt.savefig("visuals/correlation_matrix.png")
    plt.close()

if __name__ == "__main__":
    df = load_and_clean_data()
    plot_gross_distribution(df)
    plot_feature_correlation(df)
    print("Visuals generated and saved to /visuals/")
