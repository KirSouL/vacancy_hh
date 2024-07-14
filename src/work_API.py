import json
import requests
from abc import ABC, abstractmethod


class BaseHH(ABC):
    """Класс-конструктор для работы с API"""
    @abstractmethod
    def __init__(self):
        pass


class Parser(BaseHH):

    def __init__(self, file_worker):
        self.file_worker = file_worker

    def save_in_file(self, vacancies):
        """
        Метод класса Parser(BaseHH) записывающий в файл *.json всю информацию по вакансиям
        :param vacancies: список вакансий полученных с сайта hh.ru по запросу
        """
        with open(self.file_worker, "w", encoding="utf-8") as file:
            json.dump(vacancies, file, indent=4)


class HH(Parser):
    """Класс для работы с API HeadHunter"""

    def __init__(self, file_worker):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []
        super().__init__(file_worker)

    def load_vacancies(self, keyword):
        """
        Метод класса HH(Parser), который запрашивает информацию по вакаснсиям на сайте hh.ru
        :param keyword: наименовании запрашиваемой вакансии
        """
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params, timeout=10)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
        super().save_in_file(self.vacancies)


# one = HH("../data/vacancies_base.json")
# one.load_vacancies("Программист")
# print(one.vacancies)
# print(one.vacancies)

# with open("../data/vacancies_base.json", "r", encoding="utf-8") as file:
#     file_ = json.load(file)
#     for f in file_:
#         print(f["area"]["name"])

        # print(f["area"]["name"])
        # print(f["area"]["id"])
        # print("\n")
    # print(file_[12]["snippet"]["requirement"])
    # print(file_[12]["schedule"]["name"])
    # print(file_[12]["type"]["name"])
    # print(file_[10]["area"]["name"])
    # print(file_[10]["area"]["id"])
    # print(file_[12]["employment"]["name"])
    # print(file_[12]["professional_roles"][0]["name"])
    # print(file_[12]["snippet"]["responsibility"])

