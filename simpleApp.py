import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
    ## Simple Stock Price App
         
    Shown are stock opening price, closing price, volume sold, and dividends paid for **Walmart**.

""")


symbol = 'WMT'
# call Ticker in yfinance
tickerInfo = yf.Ticker(symbol)
# Get historical data for the past 10 years
tickerDF = tickerInfo.history(period='1d', start = '2014-12-01', end='2024-12-01')

st.write(""" 
         #### Opening Price
         """)
st.line_chart(tickerDF.Open)
st.write(""" 
         #### Closing Price
         """)
st.line_chart(tickerDF.Close)
st.write(""" 
         #### Volume Sold
         """)
st.line_chart(tickerDF.Volume)
st.write(""" 
         ####  Dividends Paid
         """)
st.line_chart(tickerDF.Dividends)

'''
Notes:

https://pypi.org/project/yfinance/
opwn High Low Close Volume Dividends Stock Splits

Ticker: single ticker data
Tickers: multiple tickers' data
download: download market data for multiple tickers
Search: quotes and news from search
Sector and Industry: sector and industry information
EquityQuery and Screener: build query to screen market

Get info
import yfinance as yf

msft = yf.Ticker("MSFT")

# Get all stock info
print(msft.info)

# Get historical market data
hist = msft.history(period="1mo")
print(hist)

Finanical Data
# Get dividends
print(msft.dividends)

# Get balance sheet
print(msft.balance_sheet)

# Get cash flow statement
print(msft.cashflow)

Historical Data
# Get historical data for the past 6 months
hist = msft.history(period="6mo")
print(hist)

Multiple Tickers
tickers = yf.Tickers('MSFT AAPL GOOGL')

# Access each ticker's info
print(tickers.tickers['MSFT'].info)
print(tickers.tickers['AAPL'].history(period="1mo"))
print(tickers.tickers['GOOGL'].actions)

Using a proxy server
msft = yf.Ticker("MSFT")
msft.history(proxy="PROXY_SERVER")

https://www.youtube.com/watch?v=JwSS70SZdyM
'''
