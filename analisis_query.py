import sqlite3
import pandas as pd

conn = sqlite3.connect('retail_database.db')

print ("=" * 156)
print ("=" * 156)
print ("1.  Total Revenue Per Category")
print ("=" * 156)

query_category = """
SELECT
    "Category",
    COUNT("Transaction ID") AS Total_Transactions,
    ROUND(SUM("Total Spent"), 2) AS Total_Revenue
FROM Transactions
GROUP BY "Category"
ORDER BY Total_Revenue DESC;
"""

df_category = pd.read_sql_query(query_category, conn)
print (df_category)

print ("=" * 156)
print ("2.  Favorite Payment Method In Each Location")
print ("=" * 156)

query_payment = """
SELECT
    "Location",
    "Payment Method",
    COUNT ("Transaction ID") AS Total_Transactions
FROM Transactions
GROUP BY "Location", "Payment Method"
ORDER BY "Location", Total_Transactions DESC;
"""

df_payment = pd.read_sql_query(query_payment, conn)
print (df_payment)
print ("=" * 156)
conn.close()