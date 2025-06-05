import pandas as pd

df = pd.read_csv("employee_data.csv")

mean_salary = df["MonthlySalary"].mean()
std_dev_salary = df["MonthlySalary"].std()

upper_bound = mean_salary + 3 * std_dev_salary
lower_bound = mean_salary - 3 * std_dev_salary


outliers = df[(df["MonthlySalary"] > upper_bound) | (df["MonthlySalary"] < lower_bound)]


print(outliers[["EmployeeID", "Name", "Position", "MonthlySalary"]])
