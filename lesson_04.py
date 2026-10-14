# Я прислушался

age = int(input("Введите возраст:  "))
has_ticket = input("Есть билет(да/нет):  ")
drink_alcohol = input("Вы пьяны?(да/нет)  ")

total = 0

if age < 18:
    print("Приходите когда повзрослеете) Доступ воспрещен!")
else:
    total+=1

if has_ticket.lower() != "да":
    print("В следующий раз не забудьте купить/принести билет) Доступ воспрещен!")
else:
    total+=1

if drink_alcohol.lower() != "нет":
    print("Под алкоголем вход запрещен!")
else:
    total+=1

if total == 3:
    print("Всё в порядке, проходите! Приятно провести время)")
elif total == 0:
    print("Пришел удачу испытать? Проваливай!")