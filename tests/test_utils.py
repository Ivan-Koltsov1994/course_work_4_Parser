from project_classes.engine import HH, SuperJob
from project_classes.vacancy import HHVacancy, SJVacancy
from project_utils.utils import get_vacancies,get_top_vacancies,get_top_vacancies_by_date, check_vacancy


def test_get_vacancies(vacancies):
    """Тестируем ожидаемое получение экземпляров HHVacancy/SJVacancy"""
    assert isinstance(get_vacancies(vacancies), list)
