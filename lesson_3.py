age_input = int(input("Сколько Вам лет:   "))

if age_input > 100 or age_input < 0:
    print("Введите верные значения!")
elif age_input >= 65:
    print("Вы пенсионер!")
elif  age_input >= 18:
    print("Вы взрослый!")
elif age_input >=13:
    print("Вы подросток")
else:
    print("Ты кто, пупс?")
