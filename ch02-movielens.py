# Python for Data Analysis: Ch 02 MovieLens 1M Data Set
# 4/20/2016
# @totallygloria

"""
This code snippet comes from Ch 02 of Python for Data Analysis by Wes McKinney
(O'Reilly: Sebastopol, CA, 2014). See page 22-28 for more information.
"""


import pandas as pd


# In the printed edition of the book, McKinney uses pd.read_table
# On github, he uses pd.read_csv -- the data isn't technically comma-separated, so the
# distinction here is unclear. Both seem to load the data correctly.
unames = ['user_id', 'gender', 'age', 'occupation_id', 'zipcode']
users = pd.read_csv('ch02/movielens/users.dat', sep='::', header=None, names=unames, engine='python')

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('ch02/movielens/ratings.dat', sep="::", header=None, names=rnames, engine='python')

mnames = ['movie_id', 'title', 'genre']
movies = pd.read_table('ch02/movielens/movies.dat', sep="::", header=None, names=mnames, engine='python')

# Check that the data loaded correctly:
#print users[:5]
#print ratings[:5]
#print movies[:5]


# Because it's easier to analyze the data when it's in one table, we'll use
# pandas merge function first merging ratings and users, then adding movies.

combined_data = pd.merge(pd.merge(ratings, users), movies)
#print combined_data[:5]
#print combined_data.ix[0]


# To aggregate the ratings grouped by one or more attribute, use pandas pivot_table method.
# Here's the mean movie rating grouped by gender:

mean_ratings = combined_data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')
#print mean_ratings[:5]


# let's filter this list down to movies that received 250 ratings (arbitrarily chosen)
# group the data by title using size() to get a series

ratings_by_title = combined_data.groupby('title').size()
#print ratings_by_title[:10]

active_titles = ratings_by_title.index[ratings_by_title >= 250]
#print active_titles

inactive_titles = ratings_by_title.index[ratings_by_title <= 100]
#print inactive_titles

mean_ratings = mean_ratings.ix[active_titles]
#print mean_ratings


# Let's group the top film ratings for female viewers

top_female_ratings = mean_ratings.sort_index(by='F', ascending=False)
#print top_female_ratings[:25]


# To find the greatest disagreements on ratings by gender, you can add a column
# to mean_ratings which contains the difference in means, then sort by it.

mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']  # women preferred
sorted_f_diff = mean_ratings.sort_values(by='diff')
#print sorted_f_diff[:10]

mean_ratings['diff'] = mean_ratings['F'] - mean_ratings['M']  # men preferred
sorted_m_diff = mean_ratings.sort_values(by='diff')
#print sorted_m_diff[:10]

# To find the largest absolute differences, use the variance, of the standard
# deviation of the ratings

rating_std_by_title = combined_data.groupby('title')['rating'].std()

# filter down to the most active titles

rating_std_by_title = rating_std_by_title.ix[active_titles]

# order by ascending values

print rating_std_by_title.sort_values(ascending=False)[:10]