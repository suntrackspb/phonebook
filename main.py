from pathlib import Path

from tabulate import tabulate

from db.header import headers
from oop.worker import Contact, PhoneBook

db = Path("data/data.txt")
contact = Contact()
worker = PhoneBook(db)

page = 1
while True:
    print(
        """
1. Показать справочник.
2. Поиск абонента.
3. Добавить абонента.
4. Изменить абонента.
5. Выход.
"""
    )
    option = input("Select options: ")
    if option == "1":
        print(worker.display_contacts(page))
        while True:
            select = input("1-вперед, 2-назад, 3-выход")
            if select == "1":
                print(worker.display_contacts(page + 1))
            if select == "2":
                print(worker.display_contacts(page - 1))
            if select == "3":
                break

    if option == "2":
        search = input("Найти в формате поле:что ищем,поле:что ищем: ")
        criteria = {}
        terms = search.split(",")
        for term in terms:
            column, value = term
            criteria[column] = value
        result = worker.search_contacts(criteria)
        table = tabulate([x.to_list() for x in result], headers, tablefmt='grid')
        print(table)
    if option == "3":
        pass

    elif option == "5":
        break
