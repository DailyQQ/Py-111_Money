from data_report import data, day, month, year


class Money:
    def __init__(self, amount=float, currency=None):
        """
        Конструктор класса Money
        :param amount: целые числа, минимальная единица измерения - 0.01
        :param currency: условное обозначение валюты
        """
        self.amount = amount
        self.currency = currency
        self.date = f"Курс валюты на {day}/{month}/{year}"

    def __str__(self) -> str:
        """
        :return: вид вывода денежной единицы
        """
        return f"{self.amount} {self.currency}"

    def compare_currency_and_object(self, other):
        if isinstance(other, Money):
            if self.currency == other.currency:
                pass
        #     else:
        #         # raise TypeError("Несоотвествие Валюты")
        #         other.compare_currency_convertor
        # else:
        #     raise ValueError("Нельзя сложить два неравнозначных объекта")

    # def arithmetic_op_value(self, other):
    #     if isinstance(other, (int, float)):
    #         pass
    #     else:
    #         NotImplemented

    def compare_currency_convertor(self, valute: str):
        """
        Конвертирование Вальты для сравнения
        :param valute:
        :return:
        """
        if valute in data["Valute"]:
            value1 = data["Valute"][self.currency]["Value"] / data["Valute"][self.currency]["Nominal"]
            value2 = data["Valute"][valute]["Value"] / data["Valute"][valute]["Nominal"]
            new_value = round(self.amount * value1 / value2, 2)
            print(f"Сравнение на {day}.{month}.{year}")
            return new_value

        elif valute == "RUB":
            value1 = data["Valute"][self.currency]["Value"]
            value2 = data["Valute"][self.currency]["Nominal"]
            new_value = round(self.amount * value1 / value2, 2)
            print(f"Сравнение на {day}.{month}.{year}")
            return new_value

        else:
            raise TypeError("Валюта не найдена")

    def convert_to_usd(self) -> float:
        """
        Конвертация в USD
        :return: возвращает сумму на счете в USD
        """
        if self.currency == "USD":
            return self.amount

        elif self.currency in data["Valute"]:
            value1 = data["Valute"][self.currency]["Value"] / data["Valute"][self.currency]["Nominal"]
            value2 = data["Valute"]["USD"]["Value"]
            self.amount = round(self.amount * value1 / value2, 2)
            self.currency = "USD"
            self.date = f"Данные на {day}.{month}.{year}"
            print(f"Конвертация в USD прошла по курсу на {day}.{month}.{year}\n{self.amount} {self.currency}")
            return self.amount

        elif self.currency == "RUB":
            self.amount = round(self.amount / data["Valute"]["USD"]["Value"], 2)
            self.currency = "USD"
            self.date = f"Данные на {day}.{month}.{year}"
            return self.amount

    def convert_to_another_currency(self, valute: str):
        if valute == self.charcode:
            print(f"Деньги находятся уже в той валюте, в которую вы хотите их конвертировать")
            return None

        elif valute in data["Valute"]:
            if self.charcode == "RUB":
                value1 = data["Valute"][valute]["Value"] / data["Valute"][valute]["Nominal"]
                self.value = round(self.value / value1, 2)
                self.charcode = valute
                self.date = f"Данные на {day}.{month}.{year}"
                print(f"Конвертация в {self.charcode} прошла по курсу "
                      f"на {day}.{month}.{year}\n{self.value} {self.charcode}")
                return self.value

            else:
                value1 = data["Valute"][self.charcode]["Value"] / data["Valute"][self.charcode]["Nominal"]
                value2 = data["Valute"][valute]["Value"] / data["Valute"][valute]["Nominal"]
                self.value = round(self.value * value1 / value2, 2)
                self.charcode = valute
                self.date = f"Данные на {day}.{month}.{year}"
                print(f"Конвертация в {self.charcode} прошла по курсу "
                      f"на {day}.{month}.{year}\n{self.value} {self.charcode}")
                return self.value

        elif valute == "RUB":
            value1 = data["Valute"][self.charcode]["Value"]
            value2 = data["Valute"][self.charcode]["Nominal"]
            self.value = round(self.value * value1 / value2, 2)
            self.charcode = valute
            self.date = f"Данные на {day}.{month}.{year}"
            print(f"Конвертация в {self.charcode} прошла по курсу "
                  f"на {day}.{month}.{year}\n{self.value} {self.charcode}")
            return self.value

        else:
            raise TypeError("Не возможно выполнить операцию")

    def __add__(self, other):
        """
        Сложение двух одинаковых экземляров класса Money
        :param other: значение которое хотим добавить
        :return: возращает сумму двух экземпляров
        """
        if other.compare_currency_and_object:
            arithmetic_op = round(self.amount + other.amount, 2)
            return Money(arithmetic_op, self.currency)
        else:
            NotImplemented

    def __sub__(self, other):
        """
        Вычитание двух одинаковых экземляров класса Money
        :param other: значение которое хотим добавить
        :return: возращает сумму двух экземпляров
        """
        if other.compare_currency_and_object:
            arithmetic_op = round(self.amount - other.amount, 2)
            return Money(arithmetic_op, self.currency)
        else:
            NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            arithmetic_op = round(self.amount * other, 2)
            return Money(arithmetic_op, self.currency)
        else:
            NotImplemented

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            arithmetic_op = round(self.amount / other, 2)
            return Money(arithmetic_op, self.currency)
        else:
            NotImplemented

    def __gt__(self, other):
        if other.compare_currency_and_object:
            if self.currency == other.currency:
                return self.amount > other.amount
            else:
                return self.amount > other.compare_currency_convertor(self.currency)
        else:
            return NotImplemented

    def __lt__(self, other):
        if other.compare_currency_and_object:
            if self.currency == other.currency:
                return self.amount < other.amount
            else:
                return self.amount < other.compare_currency_convertor(self.currency)
        else:
            return NotImplemented

    def __ge__(self, other):
        if other.compare_currency_and_object:
            if self.currency == other.currency:
                return self.amount >= other.amount
            else:
                return self.amount >= other.compare_currency_convertor(self.currency)
        else:
            return NotImplemented

    def __le__(self, other):
        if other.compare_currency_and_object:
            if self.currency == other.сurrency:
                return self.amount <= other.amount
            else:
                return self.amount <= other.compare_currency_convertor(self.currency)
        else:
            return NotImplemented

    def __eq__(self, other):
        if other.compare_currency_and_object:
            if self.charcode == other.сurrency:
                return self.amount == other.amount
            else:
                return self.amount == other.compare_currency_convertor(self.currency)
        else:
            return NotImplemented
