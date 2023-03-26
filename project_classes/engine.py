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

    def __init__(self, job: str, salary = None, number_of_pages = 100):
        """Инициализируется запросом пользователя"""
        self.par = {'text': f'{job}', 'page': 0, f'per_page': {number_of_pages}}  # Инициализируем данные по
        # названию профессии, id региона в HH, выводим количество страниц
        if salary is not None:
            self.par['salary'] = salary

    def get_request(self):
        """Метод, позволяющий запросить данные о вакансий через API и требуемые параметры"""
        try:
            response = requests.get(self.URL, self.par)
            if response.status_code == 200:
                return response.json()

        except requests.RequestException: # Ошибка получения данных
            print('Не удается получить данные')
