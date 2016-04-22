# Python for Data Analysis: Ch 02 US Baby Names 1880-2010
# 4/20/2016
# @totallygloria

"""
This code snippet comes from Ch 02 of Python for Data Analysis by Wes McKinney
(O'Reilly: Sebastopol, CA, 2014). See page 28 on for more information.
"""

import pandas as pd
import numpy as np

names1880 = pd.read_csv('ch02/names/yob1880.txt', names=['name', 'sex', 'births'])

# Check to make sure the names imported correctly
# print names1880

# For approximate total number of births in a year:

# print names1880.groupby('sex')['births'].sum()


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

# print names[:25]


# Now we can aggregate the data at the year and sex level using groupby or pivot_table

total_births = names.pivot_table('births', index='year', columns='sex', aggfunc=sum)

# print total_births.tail()

total_births.plot(title='Total births by sex and year')


def add_prop(group):
    # adds the proportion of births for a given name (a name / all births)
    # Integer division floors, so cast to float
    births = group.births.astype(float)
    group['prop %'] = (births / births.sum()) * 100

    return group

names = names.groupby(['year', 'sex']).apply(add_prop)

# print names[:10]

# Do a sanity check to make sure the total is sufficiently close to 100 (all names)
# This gives an error in pycharm, but returns True in ipython.

# np.allclose(names.groupby(['year', 'sex']).prop.sum(), 100)


def get_top1000(group):
    return group.sort_values(by='births', ascending=False)[:1000]


grouped = names.groupby(['year', 'sex'])
top1000 = grouped.apply(get_top1000)
top1000.index = np.arange(len(top1000))

# print top1000

'''
# the do-it-yourself version would be

pieces = []
for year, group in names.groupby(['year','sex']):
    pieces.append(group.sort_values(by='births', ascending=False)[:1000]
top1000 = pd.concat(pieces, ignore_index=True)
'''

# To do more interesting analysis, let's sort the top1000 into boys and girls

boys = top1000[top1000.sex == 'M']
girls = top1000[top1000.sex == 'F']

total_births = top1000.pivot_table('births', index='year', columns='name', aggfunc=sum)

# print total_births.info()

# This information can now be plotted for a handful of names using DataFrame's plot method

subset = total_births[['John', 'Eric', 'Mary', 'Gloria']]

subset.plot(subplots=True, figsize=(12,10), grid=False, title="Number of births per year for 4 names")
