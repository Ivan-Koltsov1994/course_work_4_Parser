from abc import ABC, abstractmethod
from datetime import datetime
import requests


class Engine(ABC):
    """Абстрактный класс от которого наследуются классы HH и Superjob для работы с сайтами"""

    @abstractmethod
    def get_request(self):
        """Метод для запроса вакансий через API сайта"""
        pass

    @staticmethod
    def get_connector(file_name: str):
        """ Возвращает экземпляр класса Connector """
        pass


class HH(Engine):
    """Класс для работы с сайтом HH"""

    URL = 'https://api.hh.ru/vacancies'  # Базовый URL для скачивания данных о вакансии

    def __init__(self, job: str, number_of_pages = 1000):
        """Инициализируется запросом пользователя"""
        self.par = {'text': f'{job}', 'page': 0, f'per_page': {number_of_pages}}  # Инициализируем данные по
        # названию профессии, id региона в HH, выводим количество страниц

    def get_request(self):
        """Метод, позволяющий запросить данные о вакансий через API и требуемые параметры"""
        try:
            response = requests.get(self.URL, self.par)
            if response.status_code == 200:
                return response.json()

        except requests.RequestException:  # Ошибка получения данных
            print('Не удается получить данные')

    @staticmethod
    def get_formatted_date(date: str) -> str:
        """Возвращает отформатированную дату"""
        date_format = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S+%f").strftime("%d.%m.%Y %X")
        return date_format

    def vacancy_info(self,data):
        """Метод, позволяющий получать данные о вакансии в требуемом виде (для ЗП в Рублях)"""

        info = {
            'Сайт': 'HeadHunter',
            'Имя профессии': data['name'],
            'Url вакансии': data['alternate_url'],
            'Требования': data.get('snippet').get('responsibility'),
            'Зарплата': data['salary'],
            'Дата публикации': self.get_formatted_date(data['published_at']),
            'Место работы': data['area']['name']
        }
        return info

    def get_vacancies_list(self) -> list:
        """Метод, позволяющий положить данные о вакансиях в словарь"""
        vacancy_list_rus = []  # Массив с вакансиями c ЗП в рублях
        page = 0
        print("Ищем требуемые вакансии..")

        while True:
            self.par['page'] = page
            data = self.get_request()

            for vacancy in data.get('items'):

                if vacancy.get('salary') == "RUR":
                    vacancy_list_rus.append(self.vacancy_info(vacancy))

                else:
                    vacancy_list_rus.append(self.vacancy_info(vacancy))

            if len(vacancy_list_rus) >= 500:
                break  # Прекращаем поиск при превышении длины списков в 500 позиций

            else:
                page += 1

        return vacancy_list_rus


#a= HH("Python Develop",100)
#print(a.get_vacancies_list())

