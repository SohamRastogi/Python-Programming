import pandas as pd


df = pd.read_csv("employee_data.csv")

df["JoinDate"] = pd.to_datetime(df["JoinDate"])


joined_2021 = df[df["JoinDate"].dt.year == 2021]

avg_salary_2021 = joined_2021["MonthlySalary"].mean()

print(f"Average Monthly Salary for employees who joined in 2021: {avg_salary_2021:.2f}")
