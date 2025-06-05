import matplotlib.pyplot as plt

dates = ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05",
         "2023-01-06", "2023-01-07", "2023-01-08", "2023-01-09", "2023-01-10"]
wind_speed = [5, 6, 7, 5, 6, 7, 5, 6, 7, 5]

plt.plot(dates, wind_speed, marker='o', color='b')


plt.yscale('log')

plt.title('Wind Speed over Time (Logarithmic Scale)', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Wind Speed (Log Scale)', fontsize=12)

plt.xticks(rotation=45)

plt.grid(True, which='both', linestyle='--', linewidth=0.5)


plt.tight_layout()
plt.show()
