import pandas as pd
from datetime import datetime

df = pd.read_csv("employee_data.csv")

df["JoinDate"] = pd.to_datetime(df["JoinDate"])


today = pd.Timestamp(datetime.today())

df["TenureMonths"] = (today - df["JoinDate"]).dt.days // 30  


df["TotalSalaryDuringTenure"] = df["MonthlySalary"] * df["TenureMonths"]

print(df[["EmployeeID", "Name", "Department", "TenureMonths", "TotalSalaryDuringTenure"]])
