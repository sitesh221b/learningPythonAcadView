import pandas as pd

#       QUESTION 1

data = {'Name': ['Sitesh', 'Peter', 'Sherlock', 'Tony'],
        'Age': [19, 18, 28, 45],
        'Email': ['s@gmail.com', 'p@spider.com', 's@sociopath.com', 't@iron.com'],
        'Phone': [23435634, 43254533, 32454235, 4354463565]}
df = pd.DataFrame(data)
print(df)


#       QUESTION 2

df = pd.read_csv("C:/Users/Subodh Roy/Downloads/weather.csv")
# a)
print(df.head(5))
# b)
print(df.head(10))
# c)
print(df.iloc[0:1, :].describe())
# d)
print(df.tail(5))
# e)
print(df['Location'].describe())
