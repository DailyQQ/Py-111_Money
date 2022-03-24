from class_money import Money
from data_report import data, day, month, year


class EUR(Money):
    """
    Класс для EUR
    """

    def convert_to_rub(self) -> Money:
        """
        Метод, конвертирующий валюту в рубли и создает экземпляр класса Money в рублях
        :return: возвращает экземпляр класса Money в рублях
        """
        value1 = data["Valute"][self.currency]["Value"] / data["Valute"][self.currency]["Nominal"]
        self.amount = round(self.amount * value1, 2)
        self.currency = "RUB"
        print(f"Конвертация в RUB на {day}.{month}.{year}\n{self.amount} {self.currency}")
        return Money(self.amount, "RUB")


if __name__ == '__main__':
    money = EUR(199, "EUR")
    print(money)
    money.convert_to_rub()