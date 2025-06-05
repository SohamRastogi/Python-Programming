import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = {
    "Temperature": [20, 21, 22, 23, 24],
    "Humidity": [60, 61, 62, 63, 64],
    "WindSpeed": [5, 6, 7, 5, 6],
    "Rainfall": [0, 1, 0, 1, 0]
}
df = pd.DataFrame(data)

df_melted = df.melt(var_name="Variable", value_name="Value")

g = sns.FacetGrid(df_melted, col="Variable", col_wrap=2, sharex=False, sharey=False)
g.map_dataframe(sns.histplot, x="Value", bins=5, color="skyblue", edgecolor="black")


plt.tight_layout()
plt.show()
