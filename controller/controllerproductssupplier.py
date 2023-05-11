import os
import sys
from prettytable import PrettyTable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dao.daoclasses import *

class ControllerProductsSupplier:
    @classmethod
    def display(cls, table_base="ProductsSupplier", *args):
        print("====================================================")
        table = PrettyTable([*args])
        data = DaoClient.get_all(table_base)
        [table.add_row(row) for row in data]

        return table
    
    @classmethod
    def add_new(cls):
        name = input("Digite o nome do produto: ")
        stock = input("Digite a quantidade: ")
        price = input("Informe o valor de venda: ")
        category = input("Categoria: ")
        print(cls.display("Supplier", "id", "nome", "contato", "cnpj"))
        id = input("Informe o ID do fornecedor: ")

        if DaoSupplierProducts.func_check_if_exists(id, 'id', "Supplier"):
            return DaoSupplierProducts.func_add("ProductsSupplier", name=name, price=price, stock=stock, 
                                         category=category, id_supplier=id)
        else:
            return 'Fornecedor nao cadastrado'
        

    @classmethod
    def edit(cls):
        pass

    @classmethod
    def delete(cls):
        pass 

if __name__ == "__main__":
    print(ControllerProductsSupplier.add_new())