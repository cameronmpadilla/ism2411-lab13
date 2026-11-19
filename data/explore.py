#1- A boolean filter is used to filter out items that you don't want to show up when you print out your code. You can set up a requirement, like only showing items that are greater than 500, and the boolean filter will only print out those values.
#2- Df['revenue'] prints out a series, while df[['revenue']] prints out a dataframe. The difference between them is that the first call prints out a 1D array and the second call prints out a 2D array.
#3- I would say that when it comes to panda, it is better than Excel because it can handle datasets of any size and you can look at all the steps leading up to the printout. It is also quicker and permenant.

# Exercise 1

import pandas as pd
df = pd.read_csv('data/retail_sales.csv')

print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

# Exercise 2

south = df[df['region'] == 'South']

print(len(south))
print(south.head())

# Exercise 3

df.sort_values('revenue', ascending=False).head(5)

print(df.sort_values('revenue', ascending=False).head(5))


# Exercise 4

big_south = df[(df['region']=='South') & (df['revenue']>1000)]

print(big_south.head(5))

# Exercise 5

df['per_unit'] = df['revenue'] / df['quantity']

print(df.head())
print(df['per_unit'].mean())

# Exercise 6

df['region'].unique()
df['region'].value_counts()

print(df['region'].unique())
print(df['region'].value_counts())

# Exercise 7

new_df = df[['region', 'product', 'revenue']]

print(new_df.shape)

# Exercise 8

df.to_csv('data/explored.csv', index=False)

import os
print(os.path.exists('data/explored.csv'))



