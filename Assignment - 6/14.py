import pandas as pd


df = pd.read_csv("employee_data.csv")

top_3_projects_by_dept = df.groupby("Department")["ProjectsHandled"].value_counts().groupby(level=0).head(3)


print(top_3_projects_by_dept)
