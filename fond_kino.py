__author__ = 'Bogdan'
__email__ = 'evstrat.bg@gmail.com'


from lxml.html import parse
import sqlite3


class SQL_backup():
    def __init__(self, test_db):
        self.connection = sqlite3.connect(test_db, check_same_thread=False)
        self.cursor = self.connection.cursor()


    def create_table(self):
        self.table = 'CREATE TABLE donor (addr INTEGER, metro TEXT)'
        self.cursor.execute(self.table)


    def insert_user(self, addr, metro):
        query = 'INSERT INTO donor VALUES ("{}", "{}")'.format(addr, metro)
        self.cursor.execute(query)
        self.connection.commit()
        return True


url = 'http://www.podari-zhizn.ru/main/node/7980'


data = parse(url)
root = data.getroot()
for elements in root.iter():
    if elements.attrib.values() == ['views-table cols-2']:
        for element in elements:
            for elem in element:
                arr = []
                for addr in elem[0]:
                    print(addr.attrib)
