from pathlib import Path
from typing import Any

from models.Contact import Contact


class PhoneBook:
    def __init__(self, file_name: Path) -> None:
        self.file_name = file_name

    def add_contact(self, contact: Contact) -> None:
        """
        Adds a contact to the file.

        Parameters:
            contact (Contact): The contact to be added.

        Returns:
            None
        """
        with self.file_name.open("a") as f:
            f.write(f"{contact.last_name},{contact.first_name},{contact.middle_name},"
                    f"{contact.organization},{contact.work_phone},{contact.personal_phone}\n")

    def edit_contact(self, contact: Contact, new_contact: Contact) -> None:
        """
        Edits a contact in the file.

        Args:
            contact (Contact): The contact to be edited.
            new_contact (Contact): The updated contact information.

        Returns:
            None
        """
        with self.file_name.open("r+") as f:
            lines = f.readlines()
            f.seek(0)
            for line in lines:
                fields = line.strip().split(',')
                if fields[:3] == [contact.last_name, contact.first_name, contact.middle_name]:
                    f.write(f"{new_contact.last_name},{new_contact.first_name},{new_contact.middle_name},"
                            f"{new_contact.organization},{new_contact.work_phone},{new_contact.personal_phone}\n")
                else:
                    f.write(line)
            f.truncate()

    def search_contacts(self, criteria: dict[str, str]) -> list[Contact]:
        """
        Search contacts in the file based on the specified criteria.
        Parameters:
            criteria (dict): A dictionary containing the criteria to search for contacts.
            The keys of the dictionary represent the fields to search for, and the values represent
            the corresponding search values.
        Returns:
            list: A list of contacts that match the specified criteria. Each contact is represented
            as an instance of the Contact class.
        """
        result = []
        with self.file_name.open() as f:
            for line in f:
                fields = line.strip().split(',')
                if all(criteria.get(key, '') in a_field for key, a_field in
                       zip(['фамилия', 'имя', 'отчество', 'компания', 'телефон раб', 'телефон моб'],
                           fields)):
                    result.append(Contact(*fields))
        return result

    def display_contacts(self, page_number: int, page_size: int = 10) -> Any:
        """
        Display contacts based on the given page number and page size.
        Parameters:
            page_number (int): The page number to display.
            page_size (int, optional): The number of contacts to display per page. Defaults to 10.
        Returns:
            list: A list of contacts to be displayed.
        """
        with self.file_name.open() as f:
            lines = f.readlines()
            total_pages = len(lines) // page_size + 1
            page_number = min(max(page_number, 1), total_pages)
            if 1 <= page_number <= total_pages:
                start_index = (page_number - 1) * page_size
                end_index = min(start_index + page_size, len(lines))

                tab = []
                for line in lines[start_index:end_index]:
                    fields = line.strip().split(',')
                    tab.append(fields)
                return [tab, total_pages]
