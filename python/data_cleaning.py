import pandas as pd

# Load raw data
df = pd.read_csv("raw_usage.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Create new features
df["hour"] = df["date"].dt.hour

# Categorize time of day
def time_category(hour):
    if 6 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 18:
        return "Afternoon"
    else:
        return "Evening"

df["time_of_day"] = df["hour"].apply(time_category)

# Identify peak hours
df["is_peak"] = df["hour"].apply(lambda x: 1 if 11 <= x <= 15 else 0)

# Save cleaned data
df.to_csv("cleaned_usage.csv", index=False)

print("Cleaned dataset created: cleaned_usage.csv")
