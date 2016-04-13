# Python for Data Analysis: Ch 02
# 4.13.2016
# @totallygloria


import json
from pandas import DataFrame, Series
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path = 'ch02/usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path, 'rb')]

frame = DataFrame(records)

print frame.info()

tz_counts = frame['tz'].value_counts()
cy_counts = frame['cy'].value_counts()
l_counts = frame['l'].value_counts()

print tz_counts[:10]
# print cy_counts[:20]
# print l_counts[:20]

clean_tz = frame['tz'].fillna('Missing')

clean_tz[clean_tz == ''] = 'TZ Unknown'

tz_counts = clean_tz.value_counts()

print tz_counts[:10]

tz_counts[:10].plot(kind='barh', rot=0)

results = Series([x.split()[0] for x in frame.a.dropna()])

print results.value_counts()[:12]

cframe = frame[frame.a.notnull()]
operating_system = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')

print operating_system[:10]

by_tz_os = cframe.groupby(['tz', operating_system])
agg_counts = by_tz_os.size().unstack().fillna(0)

print agg_counts[:10]

indexer = agg_counts.sum(1).argsort()

print agg_counts[:20]


count_subset = agg_counts.take(indexer)[-10:]

print count_subset

count_subset.plot(kind='barh', stacked=True)
normed_subset = count_subset.div(count_subset.sum(1), axis=0)
normed_subset.plot(kind='barh', stacked=True)
