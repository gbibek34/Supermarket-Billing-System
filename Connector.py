import mysql.connector

class mydb:
    def __init__(self):
        self.conn = mysql.connector.connect(host='localhost', database='supermarket', user='root', password='360DEF93g3')
        self.my_cursor = self.conn.cursor()

    def executing(self, query, values):
        self.my_cursor.execute(query, values)
        self.conn.commit()
        return True

    def show(self, query):
        self.my_cursor.execute(query)
        return self.my_cursor.fetchall()

    def show_by(self, query, values):
        self.my_cursor.execute(query, values)
        return self.my_cursor.fetchall()

    def cleartable(self, query):
        self.my_cursor.execute(query)
        self.conn.commit()
        return True