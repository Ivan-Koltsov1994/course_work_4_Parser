from project_classes.engine import HH, SuperJob


def test_hh_str(hh):
    """Тестируем метод __str__класса HH"""
    assert hh.__str__() == "Python"


def test_hh_repr(hh):
    """Тестируем метод __repr__класса HH"""
    assert hh.__repr__() == "Данные о вакансии: Python"


def test_sj_str(sj):
    """Тестируем метод __str__класса SuperJob"""
    assert sj.__str__() == "Python"


def test_sj_repr(sj):
    """Тестируем метод __repr__класса SuperJob"""
    assert sj.__repr__() == "Данные о вакансии: Python"


def test_get_formatted_date_hh():
    """Тестируем ожидаемое поведение при форматировании даты"""
    assert HH.get_formatted_date_hh('2023-03-13T07:54:44+0300') == '13.03.2023 07:54:44'


def test_get_formatted_date_sj(sj):
    """Тестируем ожидаемое поведение при форматировании даты"""
    assert SuperJob.get_formatted_date_sj(1680387602) == '02.04.2023 03:20:02'


def test_get_request_hh(hh):
    """Тестируем что метод get_request класса HH возвращает данные"""
    assert hh.get_request() is not None


def test_get_request_sj(sj):
    """Тестируем что метод get_request класса SJ возвращает данные"""
    assert sj.get_request() is not None


def test_get_vacancies_list_hh_sj(hh,sj):
    """Тестируем ошибки метода get_vacancies_list классов HH,SJ при получении данных"""
    assert isinstance(hh.get_vacancies_list(), list)
    assert isinstance(sj.get_vacancies_list(), list)