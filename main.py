from src.work_API import HH
from src.user_interface import interface
from src.Connector import Connector


def main():
    user_input = input("Введите название вакансии: ")
    user_request = HH("../work_to_HH/data/vacancies.json")

    print("Ожидаем получения данных по вакансиям")

    user_request.load_vacancies(user_input)

    Connector().add_vacancy()
    interface()


if __name__ == "__main__":
    main()
