import csv

from datetime import datetime
import matplotlib.pyplot as plt

filename = '../data/sanfrancisco_weather_04-2019_simple.csv' # assign the file to a variable
filename1 = '../data/losangeles_weather_2019_simple.csv'

# # Part 1: Read the file
# with open(filename) as f: # open the file
#     reader = csv.reader(f) # create a reader object associated with the file
#     header_row = next(reader) # assign a variable to the next row in the csv file
#     # print(header_row)



# # Part 2: Print the headers and their positions
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#
#     for index, column_header in enumerate(header_row): # To find the index of each header, use the enumerate function
#         print(index, column_header)



# # Part 3: Extract and Read the High temperature Data
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#
#     # only get the highest temperature of each day
#     highs = [] # make an empty list
#     for row in reader: # create a for loop to go through the data
#         high = int(row[5]) # make a variable to append, int is used to ensure the loop takes integers
#         highs.append(high) # appends each integer taken from the for loop
#
# print(highs)



# # Part 4: Plot the high temperatures
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#
#     highs = []
#     for row in reader:
#         high = int(row[5])
#         highs.append(high)
#
# # Begin plotting
# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.plot(highs, c='red')
#
# # Format the plot
# plt.title('San Francisco High Temperature April 2019', fontsize=20)
# plt.xlabel('', fontsize=14)
# plt.ylabel('Temperatures (F)', fontsize=14)
# plt.tick_params(axis='both', which='major', labelsize=14)
# plt.savefig('../plots/sf1.png', dpi=100)
# plt.show()



# Part 5: Plotting the Date and Time
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get the date and high temperatures
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d') # Must match date format on CSV file
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

plt.title("SF - Daily High temperatures, April 2019", fontsize=20)

plt.xlabel('', fontsize=14)
fig.autofmt_xdate() #this is what you use to label x_axis with the date

plt.ylabel('Temperatures (F)', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.savefig('../plots/sf2.png', dpi=100)
plt.show()
