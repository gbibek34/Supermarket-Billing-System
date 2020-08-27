from Connector import mydb

class query():
    def __init__(self):
        self.exe = mydb()
        
    def add_items(self, category, name, quantity, per_piece):
        query = "INSERT INTO inventory (category, name, quantity, per_piece, amount) VALUES (%s,%s,%s,%s,%s)"
        values = (category, name, quantity, per_piece, int(quantity)*int(per_piece))
        return self.exe.executing(query, values)

    def addtocart_items(self, category, name, quantity, per_piece):
        query = "INSERT INTO bill (category, name, quantity, per_piece, amount) VALUES (%s,%s,%s,%s,%s)"
        values = (category, name, quantity, per_piece, int(quantity)*int(per_piece))
        return self.exe.executing(query, values)

    def update_items(self, category, name, quantity, per_piece, id):
        query = "UPDATE inventory SET category=%s, name=%s, quantity=%s, per_piece=%s, amount=%s WHERE id=%s"
        values = (category, name, quantity, per_piece, int(quantity)*int(per_piece), id)
        return self.exe.executing(query, values)

    def updatecart_items(self, quantity, per_piece, id):
        query = "UPDATE bill SET quantity=%s, amount=%s WHERE id=%s"
        values = ( quantity, int(quantity)*int(per_piece), id)
        return self.exe.executing(query, values)

    def fetch_items(self):
        query = "SELECT * FROM inventory"
        return self.exe.show(query)

    def fetchcart_items(self):
        query = "SELECT * FROM bill"
        return self.exe.show(query)

    def delete_items(self, values):
        query = "DELETE FROM inventory WHERE id=%s"
        values = (values,)
        return self.exe.executing(query, values)

    def deletecart_items(self, values):
        query = "DELETE FROM bill WHERE id=%s"
        values = (values,)
        return self.exe.executing(query, values)

    def fetch_category(self, values):
        query = "SELECT name FROM inventory WHERE category=%s"
        values = (values,)
        return self.exe.show_by(query, values)

    def fetch_name(self, values):
        query = "SELECT quantity,per_piece FROM inventory WHERE name=%s"
        values = (values,)
        return self.exe.show_by(query,values)

    def clear_tbl(self):
        query = "TRUNCATE TABLE bill"
        return self.exe.cleartable(query)

    
