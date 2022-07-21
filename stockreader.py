# Import statements for this project
import yfinance
import datetime
import pandas

# Each stock on yahoo finance has an acronym
stock_input = input("Input a Stock Acronym: ")

# Sees if you want to view specific data through a time period
view_dates = input("Do you want to see the given stock through a given period (Yes or No): ")

# Checks to see whether the input is yes or no
timeperiod_data = False
if view_dates == "yes" or view_dates == "Yes":
    timeperiod_data = True

# Takes in an input for the start date and the end date
if timeperiod_data:
    # Start date input
    start_data_entry = input("Enter a start date in YYYY-MM-DD format: ")
    try:
        start_year, start_month, start_day = map(int, start_data_entry.split('-'))
    except ValueError:
        print("ERROR: CHECK YOUR INPUT AGAIN TO SEE IF THE FORMAT IS CORRECT")
    except NameError:
        print("ERROR: NO LETTERS ALLOWED ONLY INPUT NUMBERS OR '-'")
    start_date = datetime.date(start_year, start_month, start_day)
    # End date input
    end_data_entry = input("Enter an end date in YYYY-MM-DD format: ")
    try:
        end_year, end_month, end_day = map(int, end_data_entry.split('-'))
    except ValueError:
        print("ERROR: CHECK YOUR INPUT AGAIN TO SEE IF THE FORMAT IS CORRECT")
    except NameError:
        print("ERROR: NO LETTERS ALLOWED ONLY INPUT NUMBERS OR '-'")
    end_date = datetime.date(end_year, end_month, end_day)

# Uses a ticker to get back a specific stock
inputted_stock = yfinance.Ticker(stock_input)

# Basic information about the inputted company
stock_long_name = inputted_stock.info['longName']
stock_industry = inputted_stock.info['industry']
stock_current_price = inputted_stock.info['currentPrice']

# Uses pandas to delete columns that are not needed
if timeperiod_data:
    # Has a start date and an end date for the data
    stock_fixed_time = inputted_stock.history(start=start_date, end=end_date)
    pandas_stock_fixed_time = pandas.DataFrame(stock_fixed_time)
    del pandas_stock_fixed_time["Dividends"]
    del pandas_stock_fixed_time["Stock Splits"]
    del pandas_stock_fixed_time["Volume"]

# Basic information about the inputted stock below
print("Stock Name: " + stock_long_name)
print("Industry: " + stock_industry)
print("Current Trading Price as of " + str(datetime.datetime.today()) + ": $" + str(stock_current_price))
if timeperiod_data:
    print("Start Date: " + str(start_date) + " End Date: " + str(end_date))
    print(pandas_stock_fixed_time)