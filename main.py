import os

from project_classes.engine import Engine, HH, SuperJob
from project_utils.utils import get_top_vacancies_by_date, get_top_vacancies, check_vacancy, get_info


def main():
    # путь к файлу с хранилищем вакансий
    path = os.path.join('project_data/all.json')
    connector = Engine.get_connector(path)

    print('Добрый день! Вы подключились к хранилищу вакансий.')
    keyword = input("Какую вакансию желаете посмотреть?\n").lower()

    #  Отслеживаем данные о вакансии на HH, SJ
    hh = HH(keyword)
    sj = SuperJob(keyword)

    # Проверяем статус получения данных
    data_hh, info_hh = hh.get_request()  # Выводим статус получения данных
    data_sj, info_sj = sj.get_request()  # Выводим статус получения данных
    if not data_hh:
        exit(f'{info_hh} c сайта HeadHunter')
    elif not data_sj:
        exit(f'{info_hh} c сайта SuperJob')
    else:
        print(f'{info_hh} c сайта HeadHunter')
        print(f'{info_hh} c сайта SuperJob')

    # Складываем вакансии в файл или выводим исключение
    if check_vacancy(hh, sj):
        all_vacancies = hh.get_vacancies_list() + sj.get_vacancies_list()
        connector.insert(all_vacancies)
    else:
        print('Такой вакансии нет')

    # Сортируем полученные вакансии для вывода

    while True:
        count_vacancy = input('Введите количество выводимых вакансий\n')
        if not count_vacancy.isdigit() or int(count_vacancy) <= 0:
            print('Количество вакансий не может быть меньше 0. Необходимо повторить попытку')
            continue
        else:
            count_vacancy = int(count_vacancy)
            break

    vacancies = connector.select({})

    # Вывод данных в меню пользователя
    while True:
        print(f'Вашему вниманию предлагаются следующие варианты выбора вакансий:\n\
                        1 - вывести {count_vacancy} последних вакансии\n\
                        2 - вывести топ-{count_vacancy} вакансий заработку\n\
                        stop - закончить работу')

        user_input = input("Введите нужный вариант\n")

        if user_input == '1':
            data = get_top_vacancies_by_date(vacancies, count_vacancy)
            get_info(data)

        elif user_input == '2':
            data = get_top_vacancies(vacancies, count_vacancy)
            get_info(data)

        elif user_input.lower() == 'stop':
            print('Программа завершает работу')
            break

        else:
            print("Такого варианта нет, попробуйте еще раз")
            continue

        print('Вам нужны еще варианты выбора вакансий? Yes/None')

        # Предлагаем дополнительное пользование парсером
        keyword_user = input().lower()

        if keyword_user == 'yes' or keyword_user == 'да':
            continue
        else:
            print('Спасибо,что пользуетесь нашим приложением!')
            break

    exit()

if __name__ == '__main__':
    main()
