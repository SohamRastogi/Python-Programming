import pandas as pd
import numpy as np

table1 = pd.read_csv("employee_data.csv")
# print(table1)

ans = table1.iloc[: , 2:4]
# print(ans)

helper1 = ans.iloc[: , 1]
array = helper1.to_numpy()
# print(array)

max_index = np.argmax(array)
# print(max_index) -> the first index contains the max salary, means the 1 row pf tje monthly salary in ans dataframe of pandas.

print("department with the maximum variance in salary is : ")
print(ans.iloc[max_index , 0])
print("the maximum variance of the department is : ")
print(ans.iloc[max_index , 1])
