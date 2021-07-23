# CSV comma separated values
# with open('./weather_data.csv') as csv_file: #using relative path
#     data = csv_file.readlines()
#     print(data)

# import csv

# with open('./weather_data.csv') as csv_file:  # open csv file with the csv module
#     data = csv.reader(csv_file)  # format data into readable and iterable
#     temperatues = []  # hold temperatures from data
#     for row in data:
#         if row[1].isnumeric():  # filter out non numerical data such as headings
#             # row[1] temperature row, transformed into integer for processing
#             temperatues.append(int(row[1]))

#     print(temperatues)

import pandas

data = pandas.read_csv('./weather_data.csv')
# print(type(data))  # dataframe object (the who table)
# print(data['temp']) # series object (column of data)

# useful panda methods
# for dataframes
# data_dictionary = data.to_dict()  # converts csv table to a dictionary

# for series
# coverts one column passed as index to a list
# temp_list = data['temp'].to_list()

# def calc_average(list_given): #average and mean are the same
#     return sum(list_given)/len(list_given)

# print(f'average temp: {round(calc_average(temp_list),2)}')

# max = data['temp'].max()
# is the same as data.temp as pandas creates a class attribute per row
# print(data.temp.max())

# get data in a row
# print(data[data.day == 'Tuesday'])
# print(data[data.temp == data.temp.max()])  # search for a value, display the whole row

# monday = data[data.day == 'Monday']
# fahrenheit = (monday.temp * 1.8) + 32
# print(fahrenheit)

#convert dictionary to dataframe csv
data_dict = {
    'students':['amy','james','angela'],
    'scores':[76,56,65]
}

data = pandas.DataFrame(data_dict)
data.to_csv('./student_scores.csv')