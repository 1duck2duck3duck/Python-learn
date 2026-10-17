tasks = []
user_tasks = input("Введите задачу или напишите 'стоп' для окончания:  ")

# Цикл для добавления новых задач
while user_tasks.lower() != "стоп":  # Незачем делать if в цикле если можно так.
    tasks.append(user_tasks)
    user_tasks = input("Введите задачу или напишите 'стоп' для окончания:  ")

# Цикл для вывода задач на каждой строке
for task in tasks:
    print(f"- {task}")

print(f"Всего задач: {len(tasks)}")