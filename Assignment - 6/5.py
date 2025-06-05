import pandas as pd

df = pd.read_csv("employee_data.csv")


increase_map = {
    "Junior": 0.10,
    "Mid": 0.15,
    "Senior": 0.20
}

df["SalaryIncrease"] = df["MonthlySalary"] * df["Position"].map(increase_map)
df["SalaryIncrease"] = df["SalaryIncrease"].round(2)

print(df[["EmployeeID", "Name", "Position", "MonthlySalary", "SalaryIncrease"]])
