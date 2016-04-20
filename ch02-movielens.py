# Python for Data Analysis: Ch 02 MovieLens 1M Data Set
# 4/20/2016
# @totallygloria

"""
This code snippet comes from Ch 02 of Python for Data Analysis by Wes McKinney
(O'Reilly: Sebastopol, CA, 2014). See page 22 onward for more information.
"""


import pandas as pd


unames = ['user_id', 'gender', 'age', 'occupation_id', 'zipcode']
users = pd.read_table('ch02/movielens/users.dat', sep='::', header=None, names=unames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('ch02/movielens/ratings.dat', sep="::", header=None, names=rnames)

mnames = ['movie_id', 'title', 'genre']
movies = pd.read_table('ch02/movielens/movies.dat', sep="::", header=None, names=mnames)


print users[:5]
print ratings[:5]
print movies[:5]