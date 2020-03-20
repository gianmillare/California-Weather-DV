import csv

filename = '../data/sanfrancisco_weather_04-2019_simple.csv' # assign the file to a variable

# # Part 1: Read the file
# with open(filename) as f: # open the file
#     reader = csv.reader(f) # create a reader object associated with the file
#     header_row = next(reader) # assign a variable to the next row in the csv file
#     # print(header_row)

## Part 2: Print the headers and their positions
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row): # To find the index of each header, use the enumerate function
        print(index, column_header)