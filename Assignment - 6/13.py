import pandas as pd

df = pd.read_csv("employee_data.csv")

print("Columns in the DataFrame:", df.columns)
print(df.head())


if "MonthlySalary" in df.columns and "PerformanceScore" in df.columns:
    
    df = df.dropna(subset=["MonthlySalary", "PerformanceScore"])
    correlations = df.groupby("Department").apply(lambda x: x["MonthlySalary"].corr(x["PerformanceScore"]))

    
    high_correlation_depts = correlations[correlations > 0.5]

    
    print(high_correlation_depts)
else:
    print("Error: The required columns 'MonthlySalary' and 'PerformanceScore' are not in the CSV.")
