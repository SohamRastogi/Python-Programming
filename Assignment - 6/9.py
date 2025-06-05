import pandas as pd

df = pd.read_csv("employee_data.csv")

avg_projects = df.groupby("Department")["ProjectsHandled"].transform("mean")


df["AboveDeptAvgProjects"] = df["ProjectsHandled"] > avg_projects

above_avg_projects = df[df["AboveDeptAvgProjects"]]


print(above_avg_projects[["EmployeeID", "Name", "Department", "ProjectsHandled"]])
