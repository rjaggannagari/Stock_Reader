# yfinance is where we get the data
import yfinance
# allows us to get time
import datetime
# makes it easier to read the data and manipulate it
import pandas
# how we graph the data
import plotly.graph_objs

# Each stock on yahoo finance has an acronym
stock_input = input("Input a Stock: ")

# Sees if you want to view specific data through a time period
view_dates = input("Do you want to see the above stock in a given time period (Yes or No)? ")

# Sees if you want to view the graph of the given time period
view_graphs = input("Do you want to see the recent data of the inputted stock in a graph format (Yes or No)? ")

# Checks to see whether the input is yes or no
timeperiod_data = False
if view_dates == "yes" or view_dates == "Yes":
    timeperiod_data = True

# Checks to see whether the input is yes or no
graph_data = False
if view_graphs == "yes" or view_graphs == "Yes":
    if timeperiod_data is False:
        graph_data = True
        period_data = input("Enter the days in between: ")
        # Only valid intervals are 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
        interval_data = input("Enter the interval: ")
        data = yfinance.download(tickers=stock_input, period=period_data, interval=interval_data, rounding=True)
        figure = plotly.graph_objs.Figure()
        figure.add_trace(plotly.graph_objs.Candlestick())
        figure.add_trace(
            plotly.graph_objs.Candlestick(x=data.index, open=data['Open'], high=data['High'], low=data['Low'],
                                          close=data['Close'], name='market data'))
        figure.update_layout(title='Given Stock Share Price', yaxis_title='Stock Price (USD)')
        figure.show()

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