import numpy as np
import pandas as pd

df = pd.read_csv("employee_data.csv")

grouped = df.groupby("Department").agg({
    "PerformanceScore": "mean",
    "MonthlySalary": "sum"
}).rename(columns={
    "PerformanceScore": "AvgPerformanceScore",
    "MonthlySalary": "TotalSalary"
}).reset_index()

sorted_df = grouped.sort_values(by=["AvgPerformanceScore", "TotalSalary"], ascending=[False, True])

top_department = sorted_df.head(1)

print(top_department)
