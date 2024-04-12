class Bank:

    def __init__(self, quantity, currency="KZT"):
        self.__quantity = quantity
        self.__currency = currency

    def top_up(self, quantity):
        self.__quantity += quantity

    def withdraw_money(self, quantity):
        if self.__quantity-quantity > 0:
            self.__quantity -= quantity
            return f"Вы сняли {quantity} денег. У вас на счете осталься {self.__quantity} денег."
        elif self.__quantity-quantity < 0:
            return f"У вас на счету недостаточно средств для снятие {quantity} денег"
        
    def converting(self, currency):
        possible_currencies = ["USD", "RUB", "KZT"]

        if currency == self.__currency:
            return "Вы уже держите эту валюту на счете."

        elif currency in possible_currencies:
            if self.__currency == "KZT":
                if currency == "RUB":
                    self.__quantity //= 6
                    return f"Вы конвентировали свои деньги в {self.__quantity} RUB"
                elif currency == "USD":
                    self.__quantity //= 456
                    return f"Вы конвентировали свои деньги в {self.__quantity} USD"
            elif self.currency == "RUB":
                if currency == "KZT":
                    self.__quantity *= 6
                    return f"Вы конвентировали свои деньги в {self.__quantity} KZT"
                elif currency == "USD":
                    self.__quantity //= 93
                    return f"Вы конвентировали свои деньги в {self.__quantity} USD"
            else:
                if currency == "RUB":
                    self.__quantity *= 92
                    return f"Вы конвентировали свои деньги в {self.__quantity} RUB"
                elif currency == "KZT":
                    self.__quantity *= 456
                    return f"Вы конвентировали свои деньги в {self.__quantity} KZT"
                
        else:
            return "Недопустимая валюта для конвертации."
                

x = Bank(500)
x.top_up(700)
print(x.withdraw_money(200))
print(x.converting("USD"))