import mysql.connector
from model.group import Group


class DbFixture:
    def __init__(self, host, name, username, password):
        self.host = host
        self.name = name
        self.username = username
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=username, password=password)

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

    def destroy(self):
        self.connection.close()
