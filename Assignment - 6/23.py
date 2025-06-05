import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data = {
    "Time": ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05", "2023-01-06"],
    "Temperature": [20, 21, 22, 23, 24, 25],
    "Humidity": [60, 61, 62, 63, 64, 60],
    "Rainfall": [0, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)
df["Time"] = pd.to_datetime(df["Time"])

stack_data = df[["Temperature", "Humidity", "Rainfall"]]
normalized = stack_data.div(stack_data.sum(axis=1), axis=0)


plt.stackplot(df["Time"], 
              normalized["Temperature"], 
              normalized["Humidity"], 
              normalized["Rainfall"], 
              labels=["Temperature", "Humidity", "Rainfall"],
              alpha=0.8)

plt.legend(loc='upper left')
plt.title("Relative Contributions of Temperature, Humidity, and Rainfall")
plt.xlabel("Date")
plt.ylabel("Relative Contribution")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
