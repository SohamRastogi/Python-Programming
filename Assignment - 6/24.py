import matplotlib.pyplot as plt
import numpy as np

windspeed = np.array([5, 6, 7, 5, 6, 7])

sorted_data = np.sort(windspeed)

cdf = np.arange(1, len(sorted_data) + 1) / len(sorted_data)

plt.plot(sorted_data, cdf, marker='o', linestyle='-', color='blue')
plt.title('CDF of WindSpeed')
plt.xlabel('WindSpeed')
plt.ylabel('Cumulative Probability')
plt.grid(True)
plt.show()
