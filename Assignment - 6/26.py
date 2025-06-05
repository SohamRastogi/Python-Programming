import pandas as pd
import matplotlib.pyplot as plt

data = {
    "time": [
        "2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04",
        "2023-01-05", "2023-01-06", "2023-01-07", "2023-01-08",
        "2023-01-09", "2023-01-10", "2023-01-11", "2023-01-12",
        "2023-01-13", "2023-01-14"
    ],
    "temperature": [
        20, 21, 22, 23, 24, 25, 26, 27,
        28, 29, 20, 21, 22, 23
    ]
}

df = pd.DataFrame(data)
df["time"] = pd.to_datetime(df["time"])

df["rolling_std"] = df["temperature"].rolling(window=14).std()

plt.figure(figsize=(12, 6))
plt.plot(df["time"], df["temperature"], label="Temperature", marker='o')
plt.plot(df["time"], df["rolling_std"], label="14-day Rolling Std Dev", linestyle='--', color='orange')
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.title("Temperature Over Time with 14-Day Rolling Standard Deviation")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.xticks(rotation=45)
plt.show()
