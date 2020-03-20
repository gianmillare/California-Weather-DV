import csv

filename = '../data/sanfrancisco_weather_04-2019_simple.csv' # assign the file to a variable

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



