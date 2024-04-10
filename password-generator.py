import random
import string

def password_generator(length, password=""):
    a = [string.ascii_letters, string.digits, string.punctuation]

    try:
        for _ in range(length):
            x = random.choice(a)
            password += random.choice(x)

        return password
    
    except Exception:
        return "Произошло ошибка!"

while True:
    try:
        permission = input("Хотите я создам пароль для вас? Да/Нет:").lower()
        if permission == "нет":
           print("Хорошо, я не буду создовать пароль для вас!")
           break
        elif permission == "да":
           length = int(input("Пишите длину пароля для генерации:"))
           print(password_generator(length))
           continue
        else:
           print("Вы ввели неправильное значение!")
           continue
    except Exception:
        print("Вы ввели неправильные данные!")
        continue