while True:
    degree_ = input("Какой градус вы хотите перевести в другую? Цельсия/Фаренгейт").lower()

    if degree_ == "цельсия":
        degree = int(input("Введите сколько градусов надо перевести:"))
        print(f"Градус Цельсия {degree} равен {degree*1.8+32} градусов Фаренгейта")
        permisssion = input("Хотите еще перевести градусов? Да/Нет").lower()
        if permisssion == "да":
            continue
        else:
            break

    elif degree_ == "фаренгейт":
        degree = int(input("Введите сколько градусов надо перевести:"))
        print(f"Градус Фаренгейт {degree} равен {(degree-32)/1.8} градусов Цельсия")
        permisssion = input("Хотите еще перевести градусов? Да/Нет").lower()
        if permisssion == "да":
            continue
        else:
            break

    else:
        print("Вы не дали правильный градус!")
        continue
