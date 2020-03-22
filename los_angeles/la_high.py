import csv

from datetime import datetime
import matplotlib.pyplot as plt


filename = '../data/losangeles_weather_2019_simple.csv'

# Part 6: Plotting a longer time frame
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

plt.title('LA - Daily High Temperatures, 2019', fontsize=20)

plt.xlabel('', fontsize=14)
fig.autofmt_xdate()

plt.ylabel('Temperature (F)', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.savefig('../plots/la1.png', dpi=100)
plt.show()