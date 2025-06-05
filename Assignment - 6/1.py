import pandas as pd

table1 = pd.read_csv("employee_data.csv")
# print(table1)
ans = table1.iloc[: , 3:6]
# print(ans)
# answer = table1[table1[2] == 2023]
# print(answer)
print("change in salaries of employees are as follows : ")

print(ans.iloc[0,0] - ans.iloc[0,1])
print(ans.iloc[1,0] - ans.iloc[1,1])
print(ans.iloc[2,0] - ans.iloc[2,1])
print(ans.iloc[3,0] - ans.iloc[3,1])
print(ans.iloc[4,0] - ans.iloc[4,1])
