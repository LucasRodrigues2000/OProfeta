import sqlite3
import pandas as pd
import yfinance as YahooFinance

#criando banco de dados.
conn = sqlite3.connect('stocks.db')

url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

# Leitura da tabela HTML como DataFrame
df = pd.read_html(url, index_col=0)[0]

# Exibição do DataFrame
print(df.to_string())

#Download Data
