from src.Connector import Connector
from prettytable import PrettyTable


def interface():

    while True:
        print(
            "Введите какой результат хотите получить:\n"
            "1. Печать топ вакансий по зарплате 'от' начальной суммы 'вилки'\n"
            "2. Печать топ вакансий по зарплате 'до' конченой суммы 'вилки'\n"
            "3. Печать варианты вакансий в выбранном городе:\n"
            "4. Печать варианты вакансий по выбранной валюте:\n"
            "!. Завершение работы\n"
        )
        user_input = str(input("Введите операцию: "))
        if user_input == "1":
            additional_parameter = int(input("Введите желаемую стартовую сумму: "))
            print_top("salary_from", additional_parameter)
        elif user_input == "2":
            additional_parameter = int(input("Введите желаемую конечную сумму: "))
            print_top("salary_to", additional_parameter)
        elif user_input == "3":
            additional_parameter = input("Введите желаемый город: ")
            print_top("area", additional_parameter)
        elif user_input == "4":
            additional_parameter = input("Введите желаемую валюту: ")
            print_top("currency", additional_parameter)
        elif user_input == "!":
            print("Подбор завершен")
            return


def print_top(*args):

    info_to_user = Connector().get_info(*args)
    user_ = int(input("Введите количество для топа вакансий: "))
    table_console = PrettyTable(["name", "url", "salary_from", "salary_to", "currency", "area", "snippet"])

    for vacancy in info_to_user[:user_]:
        table_console.add_row([vacancy["name"], vacancy["url"], vacancy["salary_from"], vacancy["salary_to"],
                               vacancy["currency"], vacancy["area"], vacancy["snippet"]])

    print(table_console)
