secret = 7 #Секретное число
user_input = int(input("Что бы попытать счастья, " \
"попробуйте угадать число:  "))
total = 1 #Счетчик попыток

while user_input != secret:
    print("Неудача: Попробуйте снова")
    if user_input < secret:
        print("Подсказка: Больше")
    else:
        print("Подсказка: Меньше")
    user_input = int(input("Ваш выбор:  "))
    total+=1
else:
    # Добавление функционала (Прислушался к отзыву)
    last_digit = int(str(total)[-1])
    if last_digit == 1 and total != 11:
        print("Вы угадали")
        print(f"Вы отгадали цифру за {total} попытку")
    elif last_digit == 0 or total == 11:
        print("Вы угадали")
        print(f"Вы отгадали цифру за {total} попыток")
    elif 1 > last_digit or last_digit < 5:
        print("Вы угадали")
        print(f"Вы отгадали цифру за {total} попытки")
    else:
        print("Вы угадали")
        print(f"Вы отгадали цифру за {total} попыток")