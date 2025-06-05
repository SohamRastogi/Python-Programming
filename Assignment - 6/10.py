import pandas as pd
from datetime import datetime

df = pd.read_csv("employee_data.csv")

df["JoinDate"] = pd.to_datetime(df["JoinDate"])


today = pd.Timestamp(datetime.today())
df["YearsAtCompany"] = (today - df["JoinDate"]).dt.days / 365.25


avg_years_by_dept = df.groupby("Department")["YearsAtCompany"].mean().round(2)

print(avg_years_by_dept)
