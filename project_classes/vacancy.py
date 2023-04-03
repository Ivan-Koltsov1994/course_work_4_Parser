class Vacancy:
    __slots__ = ('website','name', 'url', 'description', 'salary', 'date_published','place_work')

    def __init__(self, data: dict):
        self.website = data['Сайт']
        self.name = data['Название профессии']
        self.url = data['Url вакансии']
        self.description = data['Требования']
        self.salary = data.get('Зарплата')
        self.date_published = data['Дата публикации']
        self.place_work = data['Место работы']

    def __gt__(self, other):
        """Метод сравнивает даты публикации"""
        return self.date_published > other.date_published

    def __lt__(self, other):
        """Метод сравнивает даты публикации"""
        return self.date_published < other.date_published

    def __str__(self):
        return f'Вакансия: {self.name}, заработная плата: {self.get_salary()}'

    def get_salary(self) -> str:
        """Метод возвращает зарплату в отформатированном виде"""

        if self.salary is not None:

            if self.salary.get('from') not in [0, None] and self.salary.get('to') not in [0, None]:
                return f"Зарплата по вакансии {self.name} от {self.salary.get('from')} до {self.salary.get('to')} руб/мес"

            elif self.salary.get('from') == 0 or None and self.salary('to') == 0 or None:
                return f'Зарплата по вакансии {self.name} не указана'

            elif self.salary.get('from') in [0, None] and self.salary.get('to') not in [0, None]:
                return f"Зарплата по вакансии {self.name}до {self.salary.get('to')} руб/мес"

            elif self.salary.get('from') not in [0, None] and self.salary.get('to') in [0, None]:
                return f"Зарплата по вакансии {self.name} от {self.salary.get('from')} руб/мес"
        else:
            return f'Зарплата по вакансии {self.name} не указана'

class HHVacancy(Vacancy):
    """ Класс наследуется от класса Vacancy определяет вакансии на HH"""

    def __str__(self):
        return f'{self.website}: {self.name}, зарплата: {self.get_salary()}'

    def __repr__(self):
        return f'{self.website}: {self.name}, зарплата: {self.get_salary()}'

class SJVacancy(Vacancy):
    """ Класс наследуется от класса Vacancy определяет вакансии на SJ"""

    def __str__(self):
        return f'{self.website}: {self.name}, зарплата: {self.get_salary()}'

    def __repr__(self):
        return f'{self.website}: {self.name}, зарплата: {self.get_salary()}'

#data_hh = {'Сайт': 'HeadHunter', 'Название профессии': 'Разработчик Python', 'Url вакансии': 'https://hh.ru/vacancy/78473911', 'Требования': 'Работка backend части программного обеспечения. Разработка внутренних библиотек. Оптимизация узких мест в основной архитектуре продукта.', 'Зарплата': {'from': 200000, 'to': 250000, 'currency': 'RUR', 'gross': False}, 'Дата публикации': '01.04.2023 18:26:21', 'Место работы': 'Москва'}

#data_sj= {'Сайт': 'SuperJob', 'Название профессии': 'Специалист службы поддержки с техническими знаниями', 'Url вакансии': 'https://armavir.superjob.ru/vakansii/specialist-sluzhby-podderzhki-s-tehnicheskimi-znaniyami-45454698.html', 'Требования': 'Поисковая система и интернет-портал.', 'Зарплата': {'from': 15000, 'to': 39000, 'currency': 'rub'}, 'Дата публикации': '02.04.2023 20:14:51', 'Место работы': 'Армавир (Краснодарский край)'}

#a = HHVacancy(data_hh)
#print(a.salary)

#b = SJVacancy(data_sj)
#print(b.website)
#print(b.__str__())
#print(b.__repr__())