import pandas as pd

df = pd.read_csv("employee_data.csv")


avg_scores = df.groupby("Position")["PerformanceScore"].transform("mean")


df["AbovePositionAverage"] = df["PerformanceScore"] > avg_scores


above_avg_employees = df[df["AbovePositionAverage"]]

print(above_avg_employees[["EmployeeID", "Name", "Position", "PerformanceScore"]])
