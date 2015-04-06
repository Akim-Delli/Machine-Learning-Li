# The first thing to do is to import the relevant packages
# that I will need for my script,
# these include the Numpy (for maths and arrays)
# and csv for reading and writing csv files
# If i want to use something from this I need to call
# csv.[function] or np.[function] first

import csv as csv
import numpy as np

# Open up the csv file in to a Python object
csv_file_object = csv.reader(open('./csv/Titanic-training-set.csv', 'rU'))

# The next() command just skips the
# first line which is a header
# Create a variable called 'data'.
# Run through each row in the csv file,
# adding each row to the data variable
# Then convert from a list to an array
# Be aware that each item is currently
# a string in this format

header = csv_file_object.next()
data = []
for row in csv_file_object:
    data.append(row)

data = np.array(data)


# print(data[0, 3])

# The size() function counts how many elements are in
# in the array and sum() (as you would expects) sums up
# the elements in the array.

number_passengers = np.size(data[0::, 1].astype(np.float))
number_survived = np.sum(data[0::, 1].astype(np.float))
proportion_survivors = number_survived / number_passengers

# This finds where all
# the elements in the gender
# column that equals "female"
women_only_stats = data[0::, 4] == "female"

# This finds where all the
# elements do not equal
# female (i.e. male)
men_only_stats = data[0::, 4] != "female"

# We use these two new variables (women_only_stats and men_only_stats) as a "mask" on our original train data,
# so we can select only those women, and only those men on board,
#  then calculate the proportion of those who survived:

women_onboard = data[women_only_stats, 1].astype(np.float)
men_onboard = data[men_only_stats, 1].astype(np.float)

# Then we finds the proportions of them that survived
proportion_women_survived = np.sum(women_onboard) / np.size(women_onboard)
proportion_men_survived = np.sum(men_onboard) / np.size(men_onboard)

# and then print it out
print('Proportion of women who survived is {}'.format(proportion_women_survived))
print('Proportion of men who survived is {}').format(proportion_men_survived)

