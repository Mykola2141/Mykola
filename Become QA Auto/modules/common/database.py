import sqlite3


class Database():
    def __init__(self):
        self.connection = sqlite3.connect(r'C:\\Users\\ACER\\Githubproject\\Mykola\\Become QA Auto' + r'\\become_qa_auto.db')
        self.cursor = self.connection.cursor()

            
    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, \
                products.description, orders.order_date \
                FROM orders \
                JOIN customers ON orders.customer_id = customers.id \
                JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record


    def get_info_from_database(self):
        query = f"SELECT name FROM sqlite_master WHERE type='table';"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return [table[0] for table in record]
    
    def get_info_from_table(self,table_name):
        query = f"SELECT * FROM '{table_name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_info_from_column(self,table_name):
        query = f"PRAGMA table_info('{table_name}')"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_orders_with_customer_name(self):
        query = f"SELECT orders.id, customers.name, orders.order_date \
                FROM orders \
                INNER JOIN customers ON orders.customer_id = customers.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    