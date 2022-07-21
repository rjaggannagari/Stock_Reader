# Import statements for this project
import yfinance
import datetime

# Each stock on Yahoo Finance has an acronym
stock_input = input("Input a Stock Acronym: ")

# Uses a ticker to get back a specific stock
inputted_stock = yfinance.Ticker(stock_input)

# Basic information about the inputted company
stock_long_name = inputted_stock.info['longName']
stock_industry = inputted_stock.info['industry']
stock_current_price = inputted_stock.info['currentPrice']

# Basic information about the inputted stock below
print("Stock Name: " + stock_long_name)
print("Industry: " + stock_industry)
print("Current Trading Price: $" + str(stock_current_price))