# EXERCISE:

# Converting currency of stocks

# In this exercise, stock prices in US Dollars for the S&P 500 in 2015 have been obtained from Yahoo Finance. The files
# sp500.csv for sp500 and exchange.csv for the exchange rates are both provided to you.

# Using the daily exchange rate to Pounds Sterling, your task is to convert both the Open and Close column prices.


# INSTRUCTIONS:

# - Read the DataFrames sp500 & exchange from the files 'sp500.csv' & 'exchange.csv' respectively..
# - Use parse_dates=True and index_col='Date'.
# - Extract the columns 'Open' & 'Close' from the DataFrame sp500 as a new DataFrame dollars and print the first 5 rows.
# - Construct a new DataFrame pounds by converting US dollars to British pounds. You'll use the .multiply() method of
# dollars with exchange['GBP/USD'] and axis='rows'
# - Print the first 5 rows of the new DataFrame pounds. This has been done for you, so hit 'Submit Answer' to see the
# results!.


# CODE:

# Import pandas
import pandas as pd

# Read 'sp500.csv' into a DataFrame: sp500
sp500 = ____

# Read 'exchange.csv' into a DataFrame: exchange
exchange = ____

# Subset 'Open' & 'Close' columns from sp500: dollars
dollars = ____

# Print the head of dollars
print(dollars.head())

# Convert dollars to pounds: pounds
pounds = ____

# Print the head of pounds
print(pounds.head())