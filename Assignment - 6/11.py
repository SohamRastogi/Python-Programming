import pandas as pd

df = pd.read_csv("employee_data.csv")


top_5_by_position = df.sort_values(by=["Position", "MonthlySalary"], ascending=[True, False])

top_5_employees = top_5_by_position.groupby("Position").head(5)


print(top_5_employees[["EmployeeID", "Name", "Position", "MonthlySalary"]])
