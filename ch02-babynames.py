# Python for Data Analysis: Ch 02 US Baby Names 1880-2010
# 4/20/2016
# @totallygloria

"""
This code snippet comes from Ch 02 of Python for Data Analysis by Wes McKinney
(O'Reilly: Sebastopol, CA, 2014). See page 28 on for more information.
"""

import pandas as pd

names1880 = pd.read_csv('ch02/names/yob1880.txt', names=['name', 'sex', 'births'])

# Check to make sure the names imported correctly
# print names1880

# For approximate total number of births in a year:

#print names1880.groupby('sex')['births'].sum()


# Since the data is separated into files by year, the first thing is to combine
# them into a single file and add a year field. This is done using pandas.concat

years = range(1880, 2011)   # 2010 was the last year available at the time of printing

pieces = []
columns = ['name', 'sex', 'births']

for year in years:
    path = 'ch02/names/yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)

    frame['year'] = year
    pieces.append(frame)

# Concatenate everything into a single data frame

names = pd.concat(pieces, ignore_index=True)

#print names[:25]


# Now we can aggregate the data at the year and sex level using groupby or pivot_table

total_births = names.pivot_table('births', index='year', columns='sex', aggfunc=sum)

print total_births.tail()

total_births.plot(title='Total births by sex and year')