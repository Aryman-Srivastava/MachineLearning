import pandas as pd

# QUERY 1
from tabulate import tabulate
#
data = pd.read_csv('test.csv')
#
# # QUERY 2
# data.reset_index(inplace=True)
# print(tabulate(data, headers='keys', tablefmt='psql'))
#
# # QUERY 3
# sam20 = data.sample(n=20)
# print(tabulate(sam20, headers='keys', tablefmt='psql'))
#
# # QUERY 4
print(len(data.index))
#
# # QUERY 5
# print(data.describe())
#
# # QUERY 6
# data.dropna(how="all", axis=0, inplace=True)
# print(tabulate(data, headers='keys', tablefmt='psql'))

# QUERY 7
nonDupli = len(data.duplicated())
Dupli = len(data.index) - nonDupli
print(nonDupli, Dupli)
