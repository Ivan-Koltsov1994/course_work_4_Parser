import os

from project_classes.engine import Engine, HH, SuperJob
from project_utils.utils import get_top_vacancies_by_date, get_top_vacancies,get_vacancies,check_vacancy


def main():

    # путь к файлу с хранилишем вакансий
    path = os.path.join('project_data/all.json')
    connector = Engine.get_connector(path)

    print('Добрый день! Вы подключились к хранилищу вакансий.')
    keyword = input("Какую вакансию желаете посмотреть?\n").lower()

    #  Отслеживаем данные о вакансии на HH,SJ
    hh = HH(keyword)
    sj = SuperJob(keyword)

    #Проверяем статус получения данных
    data_hh, info_hh = hh.get_request()  # Выводим статус получения данных
    data_sj, info_sj = sj.get_request()  # Выводим статус получения данных
    if not data_hh:
        exit(f'{info_hh} c сайта HeadHunter')
    elif not data_sj:
        exit(f'{info_hh} c сайта SuperJob')
    else:
        print(f'{info_hh} c сайта HeadHunter')
        print(f'{info_hh} c сайта SuperJob')

    #Складываем вакансии в файл или выводим исключение
    if check_vacancy(hh, sj):
        all_vacancies = hh.get_vacancies_list() + sj.get_vacancies_list()
        connector.insert(all_vacancies)
    else:
        print('Такой вакансии нет')

    # Сортируем полученные вакансии для вывода
    while True:
        top_count = input('Укажите какое количество вакансий будем выводить на экран\n')
        if not top_count.isdigit() or int(top_count) <= 0:
            print('Количество должно быть целым числом больше ноля. Попробуйте еще раз')
            continue
        else:
            top_count = int(top_count)
            break

    vacancies = connector.select({})

if __name__ == '__main__':
    main()
