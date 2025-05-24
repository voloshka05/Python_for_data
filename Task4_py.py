import pandas as pd
import numpy as np

# Завантаження даних з CSV-файлів у DataFrame
customer_data = pd.read_csv("customer_data.csv", encoding='utf-8')  
order_data = pd.read_csv("order_data.csv", encoding='utf-8') 

# Створення окремих DataFrame з завантажених даних (опціонально, бо pd.read_csv вже повертає DataFrame)
customer_df = pd.DataFrame(customer_data)
order_df = pd.DataFrame(order_data)

# Злиття двох DataFrame за стовпцем 'Customer_ID'
combine_df = pd.merge(customer_data, order_data, on='Customer_ID')
print("Злиті DataFrame:\n", combine_df)

# Фільтрація: вибираємо записи, де вік більше 30 років і сума замовлення більше 100
filter_df = combine_df[(combine_df['Age'] > 30) & (combine_df['Order_Amount'] > 100)]
print("Відфільтрований DataFrame:\n", filter_df)

# Групування за ім'ям клієнта і підрахунок загальної суми замовлень для кожного
total_amount = filter_df.groupby('Name')['Order_Amount'].sum()
print("Загальна сума:\n", total_amount)
