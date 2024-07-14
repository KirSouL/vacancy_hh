import json
from abc import ABC, abstractmethod
from src.Vacancy import WorkVacancy


class BaseConnector(ABC):

    @abstractmethod
    def create_vacancy_list(self):
        pass

    @abstractmethod
    def add_vacancy(self):
        pass

    @abstractmethod
    def get_info(self, key_name: str, value_name: str | int):
        pass

    @abstractmethod
    def remove_vacancy(self):
        pass

    @abstractmethod
    def _save(self):
        pass


class Connector(BaseConnector):

    def __init__(self):
        self.vacancy_list = []
        self.finish_list = []

    def create_vacancy_list(self):
        """
        Функция получения списка вакансий с нужной информацией
        :return: список вакансий после обработки классом WorkVacancy
        """

        with open("../work_to_HH/data/vacancies_base.json", "r", encoding="utf-8") as file:
            read_vacancy_file = json.load(file)
            for item in read_vacancy_file:
                if item["salary"] is None or item["area"] is None:
                    continue
                else:
                    self.vacancy_list.append(WorkVacancy(item["name"], item["alternate_url"], item["area"]["name"],
                                                         item["salary"]["from"], item["salary"]["to"],
                                                         item["salary"]["currency"], item["snippet"]["requirement"]))
        return self.vacancy_list

    def add_vacancy(self) -> None:
        vacancy_list = self.create_vacancy_list()
        new_vac = []
        with open("../work_to_HH/data/vacancies_to_work.json", "w", encoding="utf-8") as file:
            for f in vacancy_list:
                new_vac.append({"name": f.name_vacancy, "url": f.url_vacancy, "area": f.city,
                                "salary_from": f.salary_from, "salary_to": f.salary_to,
                                "currency": f.salary_currency, "snippet": f.snippet_requirement})
            return json.dump(new_vac, file, indent=4)

    def get_info(self, key_name: str, value_name: str | int):
        self.add_vacancy()

        with open("../work_to_HH/data/vacancies_to_work.json", "r", encoding="utf-8") as file:
            top_list = json.load(file)

        top_ = sorted(top_list, key=lambda x: x[key_name], reverse=True)

        for item in top_:
            if value_name == item[key_name]:
                self.finish_list.append(item)

        return self.finish_list

    def remove_vacancy(self):
        pass

    def _save(self):
        pass


# one = Connector()
# print(one.get_info("area", "Тюмень"))

# list_ = one.get_info()
#
# def get(list_):
#     for item in list_:
#         return item["name"]
#
# get(list_)
# sorted(one.get_info(), key=lambda x: x.name, reverse=False)