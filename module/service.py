import os


class Service:
    __unit_money = {}
    __services_price = {}
    __services_limit = {}
    __names = []
    __FILE = f"{os.getcwd()}/Services.txt"

    def __init__(self):
        self.__file = open(self.__FILE, "r", encoding='utf-8')
        self.__fill_unit_money()
        self.__fill_services()

    @staticmethod
    def get_lira_count(service):
        return Service.__unit_money[service]

    @staticmethod
    def get_service_limit(service):
        return Service.__services_limit[service]

    @staticmethod
    def get_service_price(service):
        return Service.__services_price[service]

    @staticmethod
    def get_all_unit_price():
        return Service.__unit_money

    @staticmethod
    def print_services():
        for i, j in Service.__services_price.items():
            print(f"Service id : {i} Service: {Service.__names[i - 1]} Price: {j} TL")

    def add_lira(self, service):
        self.__unit_money[service] += 1
        self.__write_unit_money()

    def remove_lira(self, service):
        self.__unit_money[service] -= 1
        self.__write_unit_money()

    def use_service(self, service):
        self.__file.seek(0)
        self.__services_limit[service] -= 1
        lines = self.__file.readlines()
        line = lines[service].split(",")
        line[2] = self.__services_limit[service]

        new_line = ""
        for i in line:
            new_line += str(i) + ","
        self.__write_new_file(service, new_line[:-1])

    def __fill_services(self):
        self.__file.seek(0)
        self.__file.readline()
        lines = self.__file.readlines()
        for i in lines:
            service = i.strip().split(",")
            self.__services_price[int(service[0])] = int(''.join(filter(str.isdigit, service[len(service) - 1])))
            self.__services_limit[int(service[0])] = int(service[2])
            self.__names.append(service[1])

    def __fill_unit_money(self):
        unit = self.__read_line()

        self.__unit_money[1] = int(unit[0])
        self.__unit_money[2] = int(unit[1])
        self.__unit_money[3] = int(unit[2])
        self.__unit_money[4] = int(unit[3])
        self.__unit_money[5] = int(unit[4])

    def __write_new_file(self, service, unit):
        self.__file.seek(0)
        list_of_lines = self.__file.readlines()
        list_of_lines[service] = unit
        a_file = open(self.__FILE, "w", encoding='utf-8')
        a_file.writelines(list_of_lines)
        a_file.close()

    def __write_unit_money(self):
        self.__file.seek(0)
        unit = ""
        for i in self.__unit_money.values():
            unit += str(i) + ","

        self.__write_new_file(0, unit[:-1] + "\n")

    def __read_line(self):
        return self.__file.readline().strip().split(",")

    def close_file(self):
        self.__file.close()
