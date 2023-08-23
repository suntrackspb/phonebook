from pathlib import Path
from typing import Type

from tabulate import tabulate

from models.Contact import Contact
from service.Phonebook import PhoneBook
from utils.console import clear_console
from utils.criteria import create_criteria
from utils.header import headers

db = Path("data/base.txt")
worker = PhoneBook(db)


def request_contact_info() -> Contact:
    """
    Creates a Contact object by requesting and collecting contact information from the user.

    Returns:
        Contact: The contact information provided by the user.
    """
    return Contact(
        last_name=input("Введите Фамилию: "),
        first_name=input("Введите Имя: "),
        middle_name=input("Введите Отчество: "),
        organization=input("Введите организацию: "),
        work_phone=input("Введите рабочий телефон а формате +7(999)000-1111: "),
        personal_phone=input("Введите мобильный телефон в формате +7(999)000-1111: "),
    )


def list_to_tabulate_str(data: list) -> str:
    return tabulate(data, headers, tablefmt='grid')


def contacts_list_to_tabulate_str(data: list) -> str:
    return tabulate([x.to_list() for x in data], headers, tablefmt='grid')


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
    # show book
    if option == "1":
        contacts, total_pages = worker.display_contacts(page)
        print(list_to_tabulate_str(contacts))
        while True:
            select = input("1-вперед, 2-назад, 3-выход: ")
            if select == "1":
                if page != total_pages:
                    clear_console()
                    page += 1
                    print(f"Страница: {page}")
                    contacts, a = worker.display_contacts(page)
                    print(list_to_tabulate_str(contacts))
            if select == "2":
                if page != 1:
                    clear_console()
                    page -= 1
                    print(f"Страница: {page}")
                    contacts, a = worker.display_contacts(page)
                    print(list_to_tabulate_str(contacts))
            if select == "3":
                break
    # search user
    if option == "2":
        search = input("Найти в формате 'поле=что ищем,поле=что ищем': ")
        if "=" in search:
            criteria = create_criteria(search)
            result = worker.search_contacts(criteria)
            print(contacts_list_to_tabulate_str(result))
        else:
            print("Неверный формат ввода")

    # add user
    if option == "3":
        contact_add = request_contact_info()
        worker.add_contact(contact_add)
        print("Абонент добавлен")

    # edit user
    if option == "4":
        search_contact: Contact = Type[Contact]
        name = input("Найдем абонента. Введите: поле=что ищем: ").split("=")
        search = f"{name[0]}={name[1]}"
        criteria = create_criteria(search)
        result = worker.search_contacts(criteria)
        if len(result) == 0:
            print("Ничего не найдено")
            continue
        if len(result) > 1:
            array = []
            print("Найдено более 1 записи, выберите номер нужной")
            for i, contact in enumerate(result):
                print(f" {i} : {contact.to_str()}")
            num = int(input("Введите номер записи: "))
            old_contact = result[num]
        else:
            print(result[0].to_str())
            old_contact = result[0]

        new_contact = request_contact_info()
        worker.edit_contact(old_contact, new_contact)

    # exit
    elif option == "5":
        break
