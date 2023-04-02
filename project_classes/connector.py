import json


class Connector:
    """Класс коннектор к файлам с вакансиями. Позволяет добавлять, удалять, фильтровать данные"""

    __data_file = None

    def __init__(self, file_path: str):
        self.__data_file = file_path # путь к файлу
        self.__connect() # при инициализации записываем или создаем новый файл файлу

    @property
    def data_file(self) -> str:
        """Делаем путь к файлу методом"""
        return self.__data_file

    @data_file.setter
    def data_file(self, value: str) -> None:
        """Метод позволяет производить добавлять в файл данные"""
        self.__data_file = value
        self.__connect()

    def __connect(self) -> None:
        """Метод открывает перезаписывает данные файла или создает новый файл"""

        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)

        except FileNotFoundError:
            print("Файл не обнаружен - создаем новый файл")

            with open(self.data_file, 'w') as f:
                json.dump([], f)
            data = []

        if not isinstance(data, list):
            raise TypeError("Файл должен содержать список")

    def insert(self, data: list) -> None:
        """Метод записи данных в файл с сохранением исходных данных"""

        with open(self.__data_file, 'r', encoding='UTF-8') as file:
            data_json = json.load(file)

        with open(self.__data_file, 'w', encoding='UTF-8') as file:
            json.dump(data_json + data, file, indent=2, ensure_ascii=False)

    def select(self, query: dict) -> list:
        """Метод выбирает данные из файла по значениям словаря"""

        sorted_data = []# создаем список для отсортированных данных

        with open(self.__data_file) as f:
            data = json.load(f)

        if not query:
            print("Данных нет в файле..")
            return data

        for item in data:
            if all(item.get(key) == value for key, value in query.items()):
                sorted_data.append(item)

        if sorted_data is not  None:
            print("Данных успешно найдены..")

        return sorted_data

    def delete(self, query: dict):
        """Метод удаляет данные из файла по значениям словаря"""

        if not query:
            print("Данных нет в файле..")
            return

        with open(self.__data_file) as f:
            data = json.load(f)

        result = []
        for item in data:
            if not all(item.get(key) == value for key, value in query.items()):
                result.append(item)

        with open(self.__data_file, 'w') as file:
            json.dump(result, file)

#df = Connector('file.json')

#data_for_file = [{'id': 1, 'title': 'tet'}]
#df.insert(data_for_file)

#d = {'title': 'tet'}
#data_from_file = df.select(d)
#print(data_from_file)