# CSV comma separated values
# with open('./weather_data.csv') as csv_file: #using relative path
#     data = csv_file.readlines()
#     print(data)

import csv

with open('./weather_data.csv') as csv_file:  # open csv file with the csv module
    data = csv.reader(csv_file)  # format data into readable and iterable
    temperatues = []  # hold temperatures from data
    for row in data:
        if row[1].isnumeric():  # filter out non numerical data such as headings
            # row[1] temperature row, transformed into integer for processing
            temperatues.append(int(row[1]))

    print(temperatues)
