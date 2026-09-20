import pandas as pd

df = pd.read_csv('dataset_kotor/retail_store_sales.csv')

df['Item'] = df['Item'].fillna('Unknown')
df['Discount Applied'] = df['Discount Applied'].fillna(False)

df['Price Per Unit'] = df['Price Per Unit'].fillna(df['Price Per Unit'].median())
df['Quantity'] = df['Quantity'].fillna(df['Quantity'].median())

df['Total Spent'] = df['Total Spent'].fillna(df['Price Per Unit'] * df['Quantity'])

df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])

df['Quantity'] = df['Quantity'].astype(int)

str_columns = ['Transaction ID', 'Customer ID', 'Category', 'Item', 'Payment Method', 'Location']
for col in str_columns:
    df[col] = df[col].astype(str).str.strip().str.title()

df = df.drop_duplicates()

print ("--- Hasil Berupa Dataset Yang Sudah Bersih ---")
df.info()

df.to_csv('dataset_bersih/dataset_retail_store_sales_clean.csv', index=False)