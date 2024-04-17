import random

def quess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        quess = int(input("Введите число от 1 до 100:"))
        attempts += 1

        if quess > secret_number:
            print("Ваше число больше моего")
        elif quess < secret_number:
            print("Мое число больше вашего")
        else:
            print(f"Воздравляю! Вы угадали число! Это заняло у вас {attempts} попыток")
            break

quess_the_number()