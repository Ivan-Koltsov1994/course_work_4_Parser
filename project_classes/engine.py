from abc import ABC, abstractmethod

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

class