from project_utils.utils import get_vacancies,get_top_vacancies,get_top_vacancies_by_date, check_vacancy,get_info


def test_get_vacancies(vacancies,vacancies_hh,vacancies_sj):
    """Тестируем ожидаемое получение экземпляров HHVacancy/SJVacancy"""
    assert isinstance(get_vacancies(vacancies), list)
    assert isinstance(get_vacancies(vacancies_hh), list)
    assert get_vacancies(vacancies_hh) is not None
    assert get_vacancies(vacancies_sj) is not None

def test_get_top_vacancies(vacancies_hh,vacancies_sj):
    """Тестируем сортировку по зарплате"""
    assert get_top_vacancies(vacancies_hh, 5)[0].salary == {'currency': 'UZS', 'from': 5000000, 'gross': True, 'to': 6000000}
    assert get_top_vacancies(vacancies_sj,5)[0].salary == {'currency': 'rub', 'from': 150000, 'to': 200000}

def test_get_top_vacancies_by_date(vacancies_hh,vacancies_sj):
    """Тестируем сортировку  по дате от большей к меньшей"""
    assert get_top_vacancies_by_date(vacancies_hh, 20)[0].date_published == "31.03.2023 22:46:17"
    assert get_top_vacancies_by_date(vacancies_hh, 20)[-1].date_published == "31.03.2023 17:44:18"
    assert get_top_vacancies_by_date(vacancies_sj, 20)[0].date_published == "31.03.2023 22:22:00"
    assert get_top_vacancies_by_date(vacancies_sj, 20)[-1].date_published == "03.04.2023 20:05:55"

def test_check_vacancy(hh,sj):
    """Тестируем метод проверки существования вакансии"""
    assert check_vacancy(hh, sj) is True