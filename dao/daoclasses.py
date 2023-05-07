from .daobase import Table
from datetime import datetime


class DaoClient(Table):
    def __init__(self):
        fields = {
            'id': "INTEGER PRIMARY KEY AUTOINCREMENT",
            'name': 'TEXT', 
            'cpf': 'TEXT',
            'active': 'BOOLEAN NOT NULL DEFAULT 1'           
        }
        super().__init__("Client", fields, "database.db")
           

class DaoEmployee(Table):
    def __init__(self):
        fields = {
            'id': "INTEGER PRIMARY KEY AUTOINCREMENT",
            'name': 'TEXT', 
            'cpf': 'TEXT',    
            'salary': 'REAL',  
            'office': 'TEXT',
            'active': 'BOOLEAN NOT NULL DEFAULT 1'     
        }
        super().__init__("Employee", fields, "database.db")
    

class DaoProducts(Table):
    def __init__(self):
        fields = {
            'id': "INTEGER PRIMARY KEY AUTOINCREMENT",
            'name': 'TEXT', 
            'purchase_price': 'REAL',
            'suplier': 'TEXT',
            'stock': 'INTEGER',
            'category': 'TEXT'
        }
        super().__init__("Products", fields, "database.db")


class DaoSupplier(Table):
    def __init__(self):
        fields = {
            'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
            'name': 'TEXT',
            'contact': 'TEXT',
            'cnpj': 'TEXT'
        }
        super().__init__("Supplier", fields, "database.db")


class DaoSupplierProducts(Table):
    def __init__(self):
        fields = {
            'id': "INTEGER PRIMARY KEY AUTOINCREMENT",
            'name': 'TEXT', 
            'price': 'REAL',
            'stock': 'INTEGER',
            'category': 'TEXT',
            'id_supplier': 'INTEGER',
            'foreign key(id_supplier)': 'REFERENCES Supplier(id)'
        }
        super().__init__("ProductsSupplier", fields, "database.db")


class DaoSales(Table):
    def __init__(self):
        fields = {
            'id': "INTEGER PRIMARY KEY AUTOINCREMENT",
            'id_employee': 'INTEGER',
            'id_client': 'INTEGER',
            'id_product': 'INTEGER',
            'amount': 'INTEGER',
            'sale_value': 'REAL',
            'date': 'DATE',    
            'foreign key(id_employee)': 'REFERENCES Employee(id)',
            'foreign key(id_client)': 'REFERENCES Client(id)',
            'foreign key(id_product)': 'REFERENCES Product(id)' 
        }
        super().__init__("Sales", fields, "database.db")


if __name__ == '__main__':
    a = DaoSales()
    b = DaoSupplier()
    


