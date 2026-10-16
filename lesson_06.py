# Задача состоит из 3-х частей, что-ж, уйдет немного больше времени
# нежели обычно...


# Часть 1. Таблица умножения
input_user = int(input(
    "Введите цифру(число), по которой хотите увидеть умножение:  "
))

for i in range(1, 11):
    multi_input = i * input_user
    print(f"{input_user} x {i} = {multi_input}")
input("Press Enter for continue: ")

# Часть 2. Поиск первого числа.
for num in range(1, 1001):
    if num % 3 == 0 and num % 7 == 0:
        print(num)
        break
input("Press Enter for continue: ")

# Часть 3. Пропуск чисел.
for i in range(1, 31):
    if i % 3 == 0:
        continue
    print(i)