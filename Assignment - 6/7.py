import pandas as pd
from datetime import datetime

df = pd.read_csv("employee_data.csv")

df["JoinDate"] = pd.to_datetime(df["JoinDate"])

today = pd.Timestamp(datetime.today())
df["YearsAtCompany"] = (today - df["JoinDate"]).dt.days / 365.25

filtered = df[(df["YearsAtCompany"] > 5) & (df["ProjectsHandled"] > 5)]

print(filtered[["EmployeeID", "Name", "JoinDate", "YearsAtCompany", "ProjectsHandled"]])
