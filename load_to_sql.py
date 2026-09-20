import sqlite3
import pandas as pd

df = pd.read_csv('dataset_bersih/dataset_retail_store_sales_clean.csv')

conn = sqlite3.connect('retail_database.db')

df.to_sql('transactions', conn, if_exists='replace', index=False)

print ("Dataset berhasil dimasukan ke database SQLite (retail_database.db) !")

query = "SELECT Category, SUM(Total_Spent) AS Total_Revenue FROM transactions GROUP BY Category ORDER BY Total_Revenue DESC"