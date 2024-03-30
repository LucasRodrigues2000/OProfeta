import sqlite3
import pandas as pd
import yfinance as YahooFinance

#criando banco de dados.
conn = sqlite3.connect('stocks.db')

#Download Data

