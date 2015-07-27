import mysql.connector
from model.group import Group
from model.contact import Contact


class DbFixture:
    def __init__(self, host, name, username, password):
        self.host = host
        self.name = name
        self.username = username
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=username, password=password)
        self.connection.autocommit = True


    def get_groups_list(self):
        groups_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (group_id, name, header, footer) = row
                groups_list.append(Group(group_id=str(group_id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
            return groups_list

    def get_contacts_list(self):
        contacts_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (contact_id, first_name, last_name) = row
                contacts_list.append(Contact(contact_id=str(contact_id), first_name=first_name, last_name=last_name))
        finally:
            cursor.close()
            return contacts_list

    def get_full_contacts_list(self):
        contacts_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id, firstname, lastname, address, home, mobile, phone2, email, email2, email3 from addressbook where deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (contact_id, first_name, last_name, address, home, mobile, phone2, email, email2, email3) = row
                contacts_list.append(
                    Contact(contact_id=str(contact_id), first_name=first_name, last_name=last_name, address=address,
                            home_phone=home, mobile_phone=mobile, phone2=phone2, email=email, email2=email2,
                            email3=email3))
        finally:
            cursor.close()
            return contacts_list

    def destroy(self):
        self.connection.close()
