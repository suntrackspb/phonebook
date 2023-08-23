class Contact:
    def __init__(self,
                 last_name: str,
                 first_name: str,
                 middle_name: str,
                 organization: str,
                 work_phone: str,
                 personal_phone: str,
                 ):
        self.last_name = last_name.capitalize()
        self.first_name = first_name.capitalize()
        self.middle_name = middle_name.capitalize()
        self.organization = organization
        self.work_phone = work_phone
        self.personal_phone = personal_phone

    def to_list(self):
        """
        Return a list containing the last name, first name, middle name, organization, work phone,
        and personal phone of the object.
        """
        return [self.last_name, self.first_name, self.middle_name, self.organization, self.work_phone,
                self.personal_phone]

    def to_str(self):
        """
        Return a string containing the last name, first name, middle name, organization, work phone,
        and personal phone of the object.
        """
        return (f"{self.last_name}, {self.first_name}, {self.middle_name}, "
                f"{self.organization}, {self.work_phone}, {self.personal_phone}")
