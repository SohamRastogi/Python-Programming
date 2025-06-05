import pandas as pd

# Extended employee data
employee_data = {
    'EmployeeID': [101, 102, 103, 104, 105],
    'Name': ['John Doe', 'Jane Smith', 'Emily Davis', 'Michael Brown', 'Sarah Wilson'],
    'Department': ['HR', 'IT', 'Finance', 'Marketing', 'Sales'],
    'MonthlySalary': [5500, 7200, 6500, 4800, 5400],
    'PreviousMonthlySalary': [5000, 7000, 6300, 4600, 5000],
    'LastPromotionDate': pd.to_datetime(['2023-05-10', '2022-08-12', '2023-11-01', '2021-02-15', '2023-01-25']),
    'JoinDate': pd.to_datetime(['2020-03-01', '2019-06-15', '2021-08-19', '2018-11-23', '2022-01-12']),
    'Age': [30, 35, 28, 40, 25],
    'Position': ['Junior', 'Senior', 'Mid', 'Junior', 'Senior'],
    'PerformanceScore': [3.8, 4.5, 4.0, 3.2, 4.7],
    'ProjectsHandled': [4, 6, 5, 7, 8]
}

# Create DataFrame
employee_df = pd.DataFrame(employee_data)
print(employee_df)
# Save to CSV
employee_df.to_csv('employee_data.csv', index=False)
