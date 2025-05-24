import pandas as pd
import numpy as np

# Читання даних із CSV-файлу
data = pd.read_csv("transaction_analysis_data.csv", encoding='utf-8')  # Вкажіть актуальний шлях до вашого файлу
df = pd.DataFrame(data)

# Розрахунок середнього чеку по кожному місту
mean_income_per_city = df.groupby('City')['Transaction_Amount'].mean()
print("Середній дохід по містах:")
print(mean_income_per_city)

# Розрахунок загального доходу для кожного міста
total_income_per_city = df.groupby('City')['Transaction_Amount'].sum()
print("\nЗагальний дохід по містах:")
print(total_income_per_city)

# Визначення індексу міста з найбільшим та найменшим доходом
highest_income_idx = total_income_per_city.argmax()
lowest_income_idx = total_income_per_city.argmin()

# Отримання назв міст за індексами
city_with_max_income = total_income_per_city.index[highest_income_idx]
city_with_min_income = total_income_per_city.index[lowest_income_idx]

# Вивід результатів
print("\nМісто з найбільшим доходом:", city_with_max_income)
print("Місто з найменшим доходом:", city_with_min_income)
