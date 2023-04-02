from project_classes.vacancy import HHVacancy, SJVacancy,Vacancy
import pytest

@pytest.fixture()
def vacancies():
    vacancies = [{'Сайт': 'HeadHunter', 'Название профессии': 'Разработчик Python (Middle, Senior)', 'Url вакансии': 'https://hh.ru/vacancy/55088580', 'Требования': 'Разрабатывать высоконагруженные системы. Платформа NGENIX ежедневно обрабатывает порядка 12 миллиардов запросов, и нам важно это делать с минимальной задержкой и...', 'Зарплата': None, 'Дата публикации': '01.04.2023 10:00:15', 'Место работы': 'Москва'},{'Сайт': 'HeadHunter', 'Название профессии': 'Программист Python (Junior)', 'Url вакансии': 'https://hh.ru/vacancy/76771861', 'Требования': 'Работа с базами данных (SQL).', 'Зарплата': {'from': 30000, 'to': None, 'currency': 'RUR', 'gross': False}, 'Дата публикации': '17.03.2023 09:27:38', 'Место работы': 'Волгоград'},{'Сайт': 'HeadHunter', 'Название профессии': 'Middle Automation Game QA Engineer (Python 3)', 'Url вакансии': 'https://hh.ru/vacancy/77493156', 'Требования': 'Заниматься ручным и автоматизированным тестированием мобильных игр. Разрабатывать документацию: тест-планы, тест-кейсы, чек-листы. Составление тест кейсов для разной...', 'Зарплата': {'from': None, 'to': 100000, 'currency': 'RUR', 'gross': False}, 'Дата публикации': '02.04.2023 16:26:30', 'Место работы': 'Санкт-Петербург'},]
    return vacancies

@pytest.fixture()
def hh_list():
    hh_list = {'Сайт': 'HeadHunter', 'Название профессии': 'Разработчик Python',
               'Url вакансии': 'https://hh.ru/vacancy/78473911',
               'Требования': 'Работка backend части программного обеспечения. Разработка внутренних библиотек. '
                             'Оптимизация узких мест в основной архитектуре продукта.',
               'Зарплата': {'from': 200000, 'to': 250000, 'currency': 'RUR', 'gross': False},
               'Дата публикации': '01.04.2023 18:26:21', 'Место работы': 'Москва'}
    return hh_list


@pytest.fixture()
def sj_list():
    sj_list = {'Сайт': 'SuperJob', 'Название профессии': 'Специалист службы поддержки с техническими знаниями', 'Url вакансии': 'https://armavir.superjob.ru/vakansii/specialist-sluzhby-podderzhki-s-tehnicheskimi-znaniyami-45454698.html', 'Требования': 'Поисковая система и интернет-портал.', 'Зарплата': {'from': 15000, 'to': 39000, 'currency': 'rub'}, 'Дата публикации': '02.04.2023 20:14:51', 'Место работы': 'Армавир (Краснодарский край)'}
    return sj_list


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

