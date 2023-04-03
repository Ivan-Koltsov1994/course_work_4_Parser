import pytest,os,json
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
def vacancies1():
    vacancies1 = {'source': 'HeadHunter', 'name': 'Python BackEnd разработчик', 'url': 'https://hh.ru/vacancy/78474203', 'description': None, 'salary': None, 'date_published': '01.04.2023 18:28:58', 'area': 'Новосибирск'}
    return vacancies1

@pytest.fixture()
def vacancies2():
    vacancies2 = {'source': 'HeadHunter', 'name': 'Python разработчик', 'url': 'https://hh.ru/vacancy/78016944', 'description': 'Разработка web-проектов на Flask, Django. Разработка парсеров, чат-ботов.', 'salary': {'from': 25000, 'to': None, 'currency': 'RUR', 'gross': False}, 'date_published': '01.04.2023 09:53:49', 'area': 'Брянск'}
    return vacancies2

@pytest.fixture()
def vacancies3():
    vacancies3 = {'source': 'HeadHunter', 'name': 'Ведущий Python разработчик (удаленно)', 'url': 'https://hh.ru/vacancy/78106381', 'description': 'Разрабатывать пайплайн для обработки большого количества исторических/риалтайм данных (100+ гигабайт). Пайплайн находит индикаторы будущих атак и считает десятки...', 'salary': {'from': None, 'to': 8000, 'currency': 'USD', 'gross': True}, 'date_published': '02.04.2023 19:32:10', 'area': 'Москва'}
    return vacancies3

@pytest.fixture()
def hh_list():
    hh_list = {'source': 'HeadHunter', 'name': 'Разработчик Python',
               'url': 'https://hh.ru/vacancy/78473911',
               'description': 'Работка backend части программного обеспечения. Разработка внутренних библиотек. '
                             'Оптимизация узких мест в основной архитектуре продукта.',
               'salary': {'from': 200000, 'to': 250000, 'currency': 'RUR', 'gross': False},
               'date_published': '01.04.2023 18:26:21', 'area': 'Москва'}
    return hh_list

@pytest.fixture()
def sj_list():
    sj_list = {'source': 'SuperJob', 'name': 'Специалист службы поддержки с техническими знаниями', 'url': 'https://armavir.superjob.ru/vakansii/specialist-sluzhby-podderzhki-s-tehnicheskimi-znaniyami-45454698.html', 'description': 'Поисковая система и интернет-портал.', 'salary': {'from': 15000, 'to': 39000, 'currency': 'rub'}, 'date_published': '02.04.2023 20:14:51', 'area': 'Армавир (Краснодарский край)'}
    return sj_list

@pytest.fixture
def path():
    return os.path.join('file_connector.json')

@pytest.fixture
def vacancies():
    path = os.path.join('test_data/all_vacancies.json')
    with open(path) as file:
        data = json.load(file)
    return data