from module.numismatic import Numismatic
from module.service import Service


class CarWashApp:

    @staticmethod
    def run():

        numismatic_app = Numismatic()
        service_app = Service()

        Numismatic.load_information()
        CarWashApp.__ask_for_money(service_app, numismatic_app)
        Service.print_services()
        while True:
            try:
                inp = int(input("Select service, press 0 to exit: "))
            except Exception as ex:
                print(ex.args)
                continue

            total_sum = numismatic_app.get_total_sum()
            process = CarWashApp.__process(inp, total_sum)
            if process == "For Money":
                print("If you want to return to the money loading screen, you can press 1 or any numeric key.")
                try:
                    x = int(input("Seçim: "))
                except Exception as ex:
                    print(ex.args)
                    continue

                if x == 1:
                    CarWashApp.__ask_for_money(service_app, numismatic_app)
                    continue
                else:
                    break
            elif process == "Exit" or process == "No Service":
                break

            service_app.use_service(inp)
            numismatic_app.spend_money(Service.get_service_price(inp))
        safe_control = CarWashApp.__decrease(numismatic_app.get_total_sum(), service_app)
        if not safe_control:
            print("We do not have enough money in our safe to return")
        service_app.close_file()

    @staticmethod
    def __ask_for_money(service_app, numismatic_app):
        while True:
            try:
                inp = int(input("Enter the amount of money, you can press 0 to exit: "))
            except Exception as ex:
                print(ex.args)
                continue

            if inp == 0:
                break
            service_app.add_lira(inp)
            numismatic_app.sum_money(inp)

    @staticmethod
    def __process(inp, total_sum):
        if inp == 0:
            return "Exit"
        if Service.get_service_limit(inp) == 0:
            print("This service is not available for purchase")
            return "No Service"
        if not CarWashApp.__control_money(Service.get_service_price(inp), total_sum):
            print("You don't have enough money")
            return "For Money"
        return "No Problem"

    @staticmethod
    def __decrease(total, service_app):
        prices_count = Service.get_all_unit_price()
        prices = Numismatic.get_all_prices()
        i = len(prices)
        while i > 0:
            price = prices[i - 1]
            if total >= price and prices_count[i] > 0:
                total -= price
                service_app.remove_lira(i)
                print(f"Return amount: {price}")
            else:
                i -= 1

        print(f"The remaining amount: {total}")
        return total == 0

    @staticmethod
    def __control_money(service_charge, total_sum):
        if service_charge > total_sum:
            return False
        return True
