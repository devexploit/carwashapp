class Numismatic:
    __prices = [5, 10, 20, 50, 100]

    def __init__(self):
        self.__sum_amount = 0

    def get_total_sum(self):
        return self.__sum_amount

    @staticmethod
    def get_all_prices():
        return Numismatic.__prices

    def spend_money(self, amount):
        self.__sum_amount -= amount

    def sum_money(self, select):
        self.__sum_amount += self.__prices[select - 1]
        print(f"Total amount uploaded: {self.__sum_amount}")

    @staticmethod
    def load_information():
        print("Welcome to the money loading screen.")
        print("1.Option 5 TL")
        print("2.Option 10 TL")
        print("3.Option 20 TL")
        print("4.Option 50 TL")
        print("5.Option 100 TL")
        print("Press 0 to exit")
