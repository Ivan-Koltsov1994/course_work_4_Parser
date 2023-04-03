from project_classes.vacancy import HHVacancy, SJVacancy


def test_init_vacancy_hh(hh_list):
    """Тестируем проверку инициализации атрибутов экземпляра класса HHVacancy"""
    hh = HHVacancy(hh_list)
    assert hh.name == "Разработчик Python"
    assert hh.url == "https://hh.ru/vacancy/78473911"
    assert hh.description == "Работка backend части программного обеспечения. Разработка внутренних библиотек. Оптимизация узких мест в основной архитектуре продукта."
    assert hh.date_published == '01.04.2023 18:26:21'
    assert hh.place_work == 'Москва'


def test_init_vacancy_sj(sj_list):
    """Тестируем проверку инициализации атрибутов экземпляра класса SJVacancy"""
    sj =SJVacancy(sj_list)
    assert sj.name == "Специалист службы поддержки с техническими знаниями"
    assert sj.url == 'https://armavir.superjob.ru/vakansii/specialist-sluzhby-podderzhki-s-tehnicheskimi-znaniyami-45454698.html'
    assert sj.description == 'Поисковая система и интернет-портал.'
    assert sj.date_published == '02.04.2023 20:14:51'
    assert sj.place_work == 'Армавир (Краснодарский край)'

def test_get_salary(hh_list):
    hh = HHVacancy(hh_list)
    pass

def test__str__hh_vacancy(hh_list):
    """Тестируем проверку __str__ класса HHVacancy"""
    hh = HHVacancy(hh_list)
    assert hh.__str__() == "HeadHunter: Разработчик Python, зарплата: Зарплата по вакансии Разработчик Python от 200000 до 250000 руб/мес"

def test__repr__hh_vacancy(hh_list):
    """Тестируем проверку __repr__ класса HHVacancy"""
    hh = HHVacancy(hh_list)
    assert hh.__repr__() == 'HeadHunter: Разработчик Python, зарплата: Зарплата по вакансии Разработчик Python от 200000 до 250000 руб/мес'

def test__str__sj_vacancy(sj_list):
    """Тестируем проверку __str__ класса SJVacancy"""
    sj = SJVacancy(sj_list)
    assert sj.__str__() == 'SuperJob: Специалист службы поддержки с техническими знаниями, зарплата: Зарплата по вакансии Специалист службы поддержки с техническими знаниями от 15000 до 39000 руб/мес'

def test__repr__sj_vacancy(sj_list):
    """Тестируем проверку __repr__ класса SJVacancy"""
    sj = SJVacancy(sj_list)
    assert sj.__repr__() == 'SuperJob: Специалист службы поддержки с техническими знаниями, зарплата: Зарплата по вакансии Специалист службы поддержки с техническими знаниями от 15000 до 39000 руб/мес'

def test_get_salary(vacancies):
    """Тестируем метод get_salary класса Vacancy"""
    hh1 = HHVacancy(vacancies[0])
    hh2 = HHVacancy(vacancies[1])
    hh3 = HHVacancy(vacancies[2])
    hh4 =HHVacancy({'Сайт': 'HeadHunter', 'Название профессии': 'Python разработчик middle+/senior', 'Url вакансии': 'https://hh.ru/vacancy/78637516', 'Требования': 'Разрабатывать сложный функционал, поддерживать и оптимизировать старый. Управлять командой разработки и самостоятельно распределять задачи внутри команды. Проводить CodeReview.', 'Зарплата': {'from': 0, 'to': None, 'currency': 'RUR', 'gross': True}, 'Дата публикации': '28.03.2023 16:43:05', 'Место работы': 'Санкт-Петербург'})

    assert hh1.get_salary() == 'Зарплата по вакансии Разработчик Python (Middle, Senior) не указана'
    assert hh2.get_salary() == 'Зарплата по вакансии Программист Python (Junior) от 30000 руб/мес'
    assert hh3.get_salary() == 'Зарплата по вакансии Middle Automation Game QA Engineer (Python 3)до 100000 руб/мес'
    assert hh4.get_salary() == 'Зарплата по вакансии Python разработчик middle+/senior не указана'

def test_gt(vacancies):
    """Тестируем метод __gt__ класса Vacancy"""

    hh1 = HHVacancy(vacancies[0])
    hh2 = HHVacancy(vacancies[1])
    assert hh1.__gt__(hh2) is False

def test_lt(vacancies):
    """Тестируем метод __lt__ класса Vacancy"""
    hh1 = HHVacancy(vacancies[0])
    hh2 = HHVacancy(vacancies[1])
    assert hh1.__lt__(hh2) is True

