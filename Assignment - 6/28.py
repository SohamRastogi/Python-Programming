import numpy as np
import matplotlib.pyplot as plt


np.random.seed(0)

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
avg_temps = [22, 24, 27, 30, 33, 35, 36, 35, 32, 28, 25, 23]

temperature_data = [np.random.normal(loc=avg, scale=2, size=30) for avg in avg_temps]

plt.figure(figsize=(12, 6))
plt.violinplot(temperature_data, showmeans=True, showmedians=True)
plt.xticks(ticks=np.arange(1, 13), labels=months)
plt.title('Monthly Temperature Distribution (Simulated)')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.grid(axis='y')
plt.tight_layout()
plt.show()
