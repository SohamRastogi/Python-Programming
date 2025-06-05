import pandas as pd

df = pd.read_csv("employee_data.csv")
dept_salary_totals = df.groupby("Department")["MonthlySalary"].transform("sum")

df["SalaryContributionPercent"] = (df["MonthlySalary"] / dept_salary_totals) * 100

result = df[["EmployeeID", "Department", "SalaryContributionPercent"]]
result["SalaryContributionPercent"] = result["SalaryContributionPercent"].round(2)

print(result)
