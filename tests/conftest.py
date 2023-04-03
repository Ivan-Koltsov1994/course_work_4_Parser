import pytest,os
from project_classes.engine import HH,SuperJob
from project_classes.connector import Connector

@pytest.fixture()
def hh():
    hh = HH('Python')
    return hh

@pytest.fixture()
def sj():
    sj = SuperJob('Python')
    return sj

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

@pytest.fixture
def path():
    return os.path.join('file_connector.json')