import csv

filename = '../data/sanfrancisco_weather_04-2019_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)