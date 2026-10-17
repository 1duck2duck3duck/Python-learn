
age = int(input("Введите возраст:  "))
has_ticket = input("Есть билет(да/нет):  ")
drink_alcohol = input("Вы пьяны?(да/нет)  ")

if age < 18:
    print("Моложе совершеннолетия нельзя!")

elif has_ticket.lower() != "да":
    print("Без билета, не пущу!")

elif drink_alcohol.lower() != "нет":
    print("Пьянчужка ступай, проспись!")

else:
    print("Всё в порядке, Приятного вечера!")
