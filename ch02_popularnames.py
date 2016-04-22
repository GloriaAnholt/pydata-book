# Python for Data Analysis: Ch 02 US Baby Names 1880-2010
# 4.22.2016
# @totallygloria

"""
These code snippets use the US gov's SSA name data from 1888-2010, and
pull from Ch 02 of Python for Data Analysis by Wes McKinney
(O'Reilly: Sebastopol, CA, 2014). See page 28 on for more information.
"""

import pandas as pd
import numpy as np


pieces = []

for year in range(1880, 2011):
    path = 'ch02/names/yob%d.txt' % year
    frame = pd.read_csv(path, names=['name', 'sex', 'births'])
    frame['year'] = year
    pieces.append(frame)


# Concatenate everything into a single data frame

names = pd.concat(pieces, ignore_index=True)

# Now we can aggregate the data at the year and sex level using groupby or pivot_table

total_births = names.pivot_table('births', index='year', columns='sex', aggfunc=sum)


def add_proportion(group):
    # adds the proportion of a name for a given year
    births = group.births.astype(float)
    group['prop %'] = (births/births.sum()) * 100

    return group

names = names.groupby(['year', 'sex']).apply(add_proportion)


def get_top_50(group):
    return group.sort_values(by='births', ascending=False)[:50]

grouped = names.groupby(['year', 'sex'])
top_50 = grouped.apply(get_top_50)
top_50.index = np.arange(len(top_50))

boys = top_50[top_50['sex'] == 'M']
girls = top_50[top_50['sex'] == 'F']

total_births = top_50.pivot_table('births', index='year', columns='name', aggfunc=sum)

subset = total_births[['John', 'Eric', 'Mary', 'Gloria']]

subset.plot(subplots=True, figsize=(12,10), grid=False, title="Number of births per year for 4 names")


