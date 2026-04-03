import pandas as pd
import numpy as np

np.random.seed(42)

n = 500

data = pd.DataFrame({
    "user_id": np.random.randint(1000, 1100, n),
    "location": np.random.choice(["Library", "Gym", "Study Room", "Cafeteria"], n),
    "date": pd.date_range(start="2024-01-01", periods=n, freq="h"),
})

# Generate start and end times
data["start_hour"] = np.random.randint(6, 22, n)
data["duration"] = np.random.randint(30, 180, n)  # minutes

# Peak hour indicator
data["is_peak"] = data["start_hour"].apply(lambda x: 1 if 11 <= x <= 15 else 0)

# Save file
data.to_csv("raw_usage.csv", index=False)

print("Dataset created: raw_usage.csv")