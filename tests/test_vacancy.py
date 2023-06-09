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
    assert sj.__str__() == 'SuperJob: Специалист службы поддержки с техническими знаниями, зарплата: Зарплата по вакансии Специалист службы поддержки с техническими знаниями от 15000 до 39000 руб/мес, дата публикации: 02.04.2023 20:14:51'

def test__repr__sj_vacancy(sj_list):
    """Тестируем проверку __repr__ класса SJVacancy"""
    sj = SJVacancy(sj_list)
    assert sj.__repr__() == 'SuperJob: Специалист службы поддержки с техническими знаниями, зарплата: Зарплата по вакансии Специалист службы поддержки с техническими знаниями от 15000 до 39000 руб/мес, дата публикации: 02.04.2023 20:14:51'

def test_get_salary(vacancies1,vacancies2,vacancies3):
    """Тестируем метод get_salary класса Vacancy"""
    hh1 = HHVacancy(vacancies1)
    hh2 = HHVacancy(vacancies2)
    hh3 = HHVacancy(vacancies3)

    assert hh1.get_salary() == 'Зарплата по вакансии Python BackEnd разработчик не указана'
    assert hh2.get_salary() == 'Зарплата по вакансии Python разработчик от 25000 руб/мес'
    assert hh3.get_salary() == 'Зарплата по вакансии Ведущий Python разработчик (удаленно)до 8000 руб/мес'


def test_gt(vacancies1,vacancies2):
    """Тестируем метод __gt__ класса Vacancy"""

    hh1 = HHVacancy(vacancies1)
    hh2 = HHVacancy(vacancies2)
    assert hh1.__gt__(hh2) is True

def test_lt(vacancies1,vacancies2):
    """Тестируем метод __lt__ класса Vacancy"""
    hh1 = HHVacancy(vacancies1)
    hh2 = HHVacancy(vacancies2)
    assert hh1.__lt__(hh2) is False

