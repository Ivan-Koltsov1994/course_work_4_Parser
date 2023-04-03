import os

from project_classes.engine import Engine, HH, SuperJob
from project_utils.utils import get_top_vacancies_by_date, get_top_vacancies,get_vacancies,check_vacancy


def main():

    # путь к файлу с хранилишем вакансий
    path = os.path.join('data/all.json')
    connector = Engine.get_connector(path)

    print('Добрый день! Вы подключились к хранилищу вакансий.')
    keyword = input("Какую вакансию желаете посмотреть?\n").lower()

if __name__ == '__main__':
    main()