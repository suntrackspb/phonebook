from tabulate import tabulate
from db.header import headers


class Contact:
    def __init__(self, last_name, first_name, middle_name, organization, work_phone, personal_phone):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.organization = organization
        self.work_phone = work_phone
        self.personal_phone = personal_phone

    def to_list(self):
        return [self.last_name, self.first_name, self.middle_name, self.organization, self.work_phone,
                self.personal_phone]


class PhoneBook:
    def __init__(self, file_name):
        self.file_name = file_name

    def add_contact(self, contact):
        with open(self.file_name, 'a') as f:
            f.write(f"{contact.last_name},{contact.first_name},{contact.middle_name},"
                    f"{contact.organization},{contact.work_phone},{contact.personal_phone}\n")

    def edit_contact(self, contact, new_contact):
        with open(self.file_name, 'r+') as f:
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

    def search_contacts(self, criteria):
        result = []
        with open(self.file_name, 'r') as f:
            for line in f:
                fields = line.strip().split(',')
                if all(criteria.get(key, '') in field for key, field in
                       zip(['фамилия', 'имя', 'отчество', 'компания', 'телефон раб', 'телефон моб'],
                           fields)):
                    result.append(Contact(*fields))
        return result

    def display_contacts(self, page_number, page_size=10):
        with open(self.file_name, 'r') as f:
            lines = f.readlines()
            total_pages = len(lines) // page_size + 1
            page_number = min(max(page_number, 1), total_pages)
            start_index = (page_number - 1) * page_size
            end_index = min(start_index + page_size, len(lines))

            tab = []
            for line in lines[start_index:end_index]:
                fields = line.strip().split(',')
                tab.append(fields)
                # print(f"{fields[0]} {fields[1]} {fields[2]} - {fields[3]} - {fields[4]} - {fields[5]}")
            table = tabulate(tab, headers, tablefmt='grid')
        return table


# df = PhoneBook("/home/sun/PycharmProjects/console-phonebook/data/data.txt")
#
# # # print(df.display_contacts(2))
# #
# criteria = {
#     "фамилия": "Денис",
# }
# r = df.search_contacts(criteria)
#
# table = tabulate([x.to_list() for x in r], headers, tablefmt='grid')
# print(table)
#
# # df.edit_contact("Денис", "Егор")
