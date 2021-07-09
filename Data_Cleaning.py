# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 10:55:52 2021

@author: sasim
"""

import pandas as pd

# Import Sales Transaction file and Customer file
sales_2017_df = pd.read_csv('C:\\Users\\sasim\\OneDrive\\Desktop\\Product-Recommendation-System\\Sales Transactions-2017.csv')
sales_2018_df = pd.read_csv('C:\\Users\\sasim\\OneDrive\\Desktop\\Product-Recommendation-System\\Sales Transactions-2018.csv')
sales_2019_df = pd.read_csv('C:\\Users\\sasim\\OneDrive\\Desktop\\Product-Recommendation-System\\Sales Transactions-2019.csv')

# Concatenate all the Sales dataframes
full_sales_df = pd.concat([sales_2017_df, sales_2018_df, sales_2019_df], ignore_index=True,sort=False)

# Drop the Columns Gross, Disc, Voucher Amount, using drop() method on the specific columns
sales_df = full_sales_df.drop(columns=['Gross','Disc','Voucher Amount'],axis=1)

# Drop the Rows with Date column being NaN (Null) or Spaces, using dropna() method and subset as only Date column
sales_df = sales_df[sales_df['Date'] != ' '].dropna(subset=['Date'])

# Convert the Date format from DD/MM/YYYY to YYYY/MM/DD (input date is with Day First), using to_datetime method
sales_df['Date'] = pd.to_datetime(sales_df['Date'],dayfirst=True)

# Remove the string'Sal:' from Voucher column, using .str.slice(start,stop,step) method
sales_df['Voucher'] = sales_df['Voucher'].str.slice(start=4,stop=None,step=1).astype(int)

# Covert the Party column into uppercase
sales_df['Party'] = sales_df['Party'].str.upper()

# Covert the Product column into uppercase
sales_df['Product'] = sales_df['Product'].str.upper()

# Convert the Qty column into an integer (Data has the entries with ',' and '.00') - Assuming Quantity can only be an integer
sales_df['Qty'] = sales_df['Qty'].str.replace(',','').astype(float).astype(int)

# Eliminate ',' in the Rate column
sales_df['Rate'] = sales_df['Rate'].str.replace(',','').astype(float)

# Convert the Rate column into float variable with e decimal points
#sales_df['Rate'] = sales_df['Rate'].apply(lambda x: round(x, 2))

# Sort the Sales Transaction file in the order of Date and Voucher
sales_df = sales_df.sort_values(['Date','Voucher'])



# Write the Edited Sales Transaction file to .csv
sales_df.to_csv('C:\\Users\\sasim\\OneDrive\\Desktop\\Product-Recommendation-System\\Sales-Transactions-Edited.csv',index=False)














































