# Требуемые импорты
from __future__ import annotations

from project_classes.engine import HH, SuperJob
from project_classes.vacancy import HHVacancy, SJVacancy


def get_vacancies(vacancies: list) -> list[HHVacancy | SJVacancy]:
    """Функция возвращает экземпляры HHVacancy/SJVacancy"""

    vacancies_list = []
    for vacancy in vacancies:
        if vacancy['source'] == "HeadHunter":
            vacancies_list.append(HHVacancy(vacancy))
        else:
            vacancies_list.append(SJVacancy(vacancy))
    return vacancies_list


def get_top_vacancies(data, top_work_count) -> list:
    """ Функция возвращает наиболее оплачиваемые вакансии"""

    # Делаем перебор данных из файла по зарплате
    vacancies_list = []
    for item in data:
        if item.get('salary') is None or item.get('salary').get('from') is None:
            continue
        else:
            vacancies_list.append(item)

    # Сортировка по зарплате
    vacancies_list.sort(key=lambda k: k['salary']['from'], reverse=True)
    top_vacancies = vacancies_list[:top_work_count]

    if len(top_vacancies) == 0:
        return "В вакансиях не указана зарплата"
    else:
        return get_vacancies(top_vacancies)


def check_vacancy(hh: HH, sj: SuperJob) -> bool:
    """Функция проверяет существование вакансии"""
    return hh.get_request()[0] != [] or sj.get_request()[0] != []


def get_top_vacancies_by_date(data: list, count: int) -> list:
    """Функция сортирует вакансии по дате публикации"""

    vacancies = get_vacancies(data)
    return sorted(vacancies, reverse=True)[:count]

def get_info(data: list | str):
    """Вывод построчно с нумерацией, если список, либо вывод строки"""
    if isinstance(data, list):
        count = 1
        for item in data:
            print(f'{count} - {item}')
            count += 1
    else:
        print(data)

