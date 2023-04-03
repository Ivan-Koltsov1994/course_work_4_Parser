# Добавляем требуемые импорты
from abc import ABC, abstractmethod
from datetime import datetime
from project_classes.connector import Connector
import requests
import os


class Engine(ABC):
    """Абстрактный класс от которого наследуются классы HH и Superjob для работы с сайтами"""

    @abstractmethod
    def get_request(self):
        """Метод для запроса вакансий через API сайта"""
        pass

    @staticmethod
    def get_connector(file_name) -> Connector:
        """ Возвращает экземпляр класса Connector """
        return Connector(file_name)


class HH(Engine):
    """Класс для работы с сайтом HH"""

    URL = 'https://api.hh.ru/vacancies'  # Базовый URL для скачивания данных о вакансии

    def __init__(self, job: str):
        """Инициализируется запросом пользователя"""
        self.job = job
        self.par = {'text': f'{self.job}', 'page': 0, 'per_page': 100}  # Инициализируем данные по
        # названию профессии, id региона в HH, выводим количество страниц


    def __str__(self):
        return f'{self.job}'

    def __repr__(self):
        return f'Данные о вакансии: {self.job}'

    @staticmethod
    def get_formatted_date_hh(date: str) -> str:
        """Возвращает отформатированную дату"""
        date_format = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S+%f").strftime("%d.%m.%Y %X")
        return date_format

    def get_request(self):
        """Метод, позволяющий запросить данные о вакансий через API и требуемые параметры"""
        try:
            response = requests.get(self.URL, self.par)
            if response.status_code == 200:
                return response.json(), 'INFO:Данные получены успешно'
            return None, f'ERROR:status_code:{response.status_code} \n'

        except requests.exceptions.JSONDecodeError:
            return None, 'ERROR:requests.exceptions.JSONDecodeError \n'

        except requests.exceptions.ConnectionError:
            return None, 'ERROR:requests.exceptions.ConnectionError \n'

    def vacancy_info(self, data):
        """Метод, позволяющий получать данные о вакансии в требуемом виде (для ЗП в Рублях)"""

        info = {
            'source': 'HeadHunter',
            'name': data['name'],
            'url': data['alternate_url'],
            'description': data.get('snippet').get('responsibility'),
            'salary': data['salary'],
            'date_published': self.get_formatted_date_hh(data['published_at']),
            'area': data['area']['name']
        }
        return info

    def get_vacancies_list(self) -> list:
        """Метод, позволяющий положить данные о вакансиях в словарь"""
        vacancy_list_rus = []  # Массив с вакансиями c ЗП в рублях
        page = 0
        print("Ищем требуемые вакансии..")

        while True:
            self.par['page'] = page
            data = self.get_request()[0]

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


class SuperJob(Engine):
    """Класс для работы с сайтом SJ"""

    URL = 'https://api.superjob.ru/2.0/vacancies/'  # Базовый URL для скачивания данных о вакансии c SJ

    def __init__(self, job: str):
        """Инициализируется запросом пользователя"""
        self.job = job
        self.par = {'keywords': f'{job}', 'count': 100, 'page': 1}
        self.HEADERS = {
            'Host': 'api.superjob.ru',
            'X-Api-App-Id': os.getenv('SJ_API_KEY'),  # Токен SJ, встроенный в переменные окружения
            'Authorization': 'Bearer r.000000010000001.example.access_token',
            'Content-Type': 'application/x-www-form-urlencoded'
        }  # Делаем запрос к API SJ

    def __str__(self):
        return f'{self.job}'

    def __repr__(self):
        return f'Данные о вакансии: {self.job}'

    @staticmethod
    def get_formatted_date_sj(date: int) -> str:
        """Возвращает отформатированную дату"""
        date_format = datetime.fromtimestamp(int(date)).strftime("%d.%m.%Y %X")
        return date_format

    def get_request(self):
        """Запрос вакансий через API"""

        try:
            response = requests.get(url=self.URL, headers=self.HEADERS, params=self.par)
            if response.status_code == 200:
                return response.json(), 'INFO:Данные получены успешно \n'
            return None, f'ERROR:status_code:{response.status_code} \n'

        except requests.exceptions.JSONDecodeError:
            return None, 'ERROR:requests.exceptions.JSONDecodeError \n'

        except requests.exceptions.ConnectionError:
            return None, 'ERROR:requests.exceptions.ConnectionError \n'

    def vacancy_info(self, data: dict) -> dict:
        """Метод, позволяющий получать данные о вакансии в требуемом виде (для ЗП в Рублях)"""
        salary = {'from': data['payment_from'],
                  'to': data['payment_to'],
                  'currency': data['currency']}
        info = {
            'source': 'SuperJob',
            'name': data['profession'],
            'url': data['link'],
            'description': data.get('client').get('description'),
            'salary': salary,
            'date_published': self.get_formatted_date_sj(str(data['date_published'])),
            'area': data['town']['title']
        }
        return info

    def get_vacancies_list(self):
        """Записывает информацию о вакансии в список при наличии сведений о ЗП в рублях"""
        vacancy_list_rus = []  # Массив с вакансиями c ЗП в рублях

        for i in range(100):
            self.par['page'] = i
            data = self.get_request()[0]

            for vacancy in data.get('objects'):
                if vacancy.get('currency') is not None:
                    if vacancy.get('currency') == "rub" or vacancy.get('currency') is None:
                        vacancy_list_rus.append(self.vacancy_info(vacancy))
                    else:
                        continue
            if len(vacancy_list_rus) >= 500:  # Прекращаем поиск при превышении длины списков в 500 позиций
                break

        return vacancy_list_rus


#hh = HH('Python')
#data,info = hh.get_request()
#print(hh.get_request())
#exit(info)
#data_hh = hh.get_vacancies_list()
#a = Engine.get_connector("../tests/test_data/vacancies_list_hh.json")
#a.insert(data_hh)



sj = SuperJob('Python')
print(sj.get_vacancies_list()[0])
#data_sj= sj.get_vacancies_list()
#b = Engine.get_connector("../tests/test_data/vacancies_list_sj.json")
#b.insert(data_sj)