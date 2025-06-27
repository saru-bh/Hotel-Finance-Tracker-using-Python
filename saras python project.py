# Hotel Finance Tracker by Saraswati Bhandari

import pandas as pd
import numpy as np


# 1. Sample data with 25 records
data = {
    'Date': pd.date_range(start='2024-01-01', periods=25, freq='W'),
    'Department': ['Front Office', 'F&B', 'Housekeeping', 'Accounts', 'Maintenance'] * 5,
    'Revenue': [50000, 80000, 20000, 0, 15000,
                55000, 75000, 25000, 0, 12000,
                60000, 72000, 18000, 0, 10000,
                58000, 79000, 23000, 0, 11000,
                62000, 81000, 22000, 0, 14000],
    'Expense': [30000, 40000, 12000, 9000, 7000,
                32000, 42000, 15000, 9500, 6500,
                31000, 43000, 11000, 8800, 7300,
                33000, 41000, 14000, 9700, 6800,
                34000, 44000, 13000, 9300, 7200],
    'Salary': [15000, 20000, 8000, 30000, 6000,
               16000, 21000, 9000, 31000, 5500,
               15500, 20500, 8500, 29500, 5800,
               16500, 21500, 9500, 30500, 5700,
               17000, 22000, 9200, 29900, 6000]}

df = pd.DataFrame(data)

# 2. Calculate net profit
df['Net_Profit'] = df['Revenue'] - (df['Expense'] + df['Salary'])

# 3. Summary by department
dept_summary = df.groupby('Department')[['Revenue', 'Expense', 'Salary', 'Net_Profit']].sum()

# 4. Summary by month
df['Month'] = df['Date'].dt.to_period('M')
month_summary = df.groupby('Month')[['Revenue', 'Expense', 'Salary', 'Net_Profit']].sum()



print("✅ Hotel Finance Tracker Completed Successfully!")
print(df)
print(dept_summary)
print(month_summary)








