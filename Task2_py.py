import pandas as pd
import numpy as np
# Завантаження CSV-файлу
data = pd.read_csv("extended_sales_data.csv", encoding='utf-8')  # Змініть шлях до свого файлу
df = pd.DataFrame(data)

print("Перші 5 рядків")
print(df.head(5)) #Виводить перші 5 рядків
print("Останні 5 рядків")
print(df.tail()) #Виводить останні 5 рядків

df_cleaned = df.dropna(axis=0, how='any')
print('Без пустих значень')
print(df_cleaned)

print("Без дублікатів")
df_wthoutdup = df_cleaned.drop_duplicates(subset=["Name"], keep='first')
print(df_wthoutdup)

df_fill = df.fillna(value={'Purchase_Amount': df['Purchase_Amount'].mean()})
print(df_fill)