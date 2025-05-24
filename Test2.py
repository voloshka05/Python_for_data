import numpy as np

# Створення випадкового 3x3 масиву зі значеннями від 1 до 100
matrix = np.random.randint(1, 101, (3, 3))
print("Згенерований масив:")
print(matrix)

# Обчислення суми всіх елементів масиву
total = np.sum(matrix)
print("\nЗагальна сума елементів:", total)

# Пошук максимального та мінімального значення разом з їхніми індексами
max_value = np.max(matrix)
min_value = np.min(matrix)
max_pos = np.unravel_index(np.argmax(matrix), matrix.shape)
min_pos = np.unravel_index(np.argmin(matrix), matrix.shape)
print("\nМаксимум:", max_value, "знаходиться на позиції", max_pos)
print("Мінімум:", min_value, "знаходиться на позиції", min_pos)

# Сортування кожного рядка по зростанню
row_sorted = np.sort(matrix, axis=1)
print("\nМасив після сортування рядків:")
print(row_sorted)