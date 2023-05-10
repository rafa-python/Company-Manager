import os
import sys
from prettytable import PrettyTable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dao.daoclasses import *

class ControllerProductsSupplier:
    @classmethod
    def display(cls):
        print("====================================================")
        table = PrettyTable(["id", "name", "price", "stock", "category", "id_supplier"])
        data = DaoClient.get_all("ProductsSupplier")
        [table.add_row(row) for row in data]

        return table
    
    @classmethod
    def add_new(cls):
        name = input("Digite o nome do produto: ")
        stock = input("Digite a quantidade: ")
        price = input("Informe o valor de venda: ")
        category = input("Categoria: ")
        print(DaoSupplier.func_display("Supplier"))
        id = input("Informe o ID do fornecedor: ")
        

    @classmethod
    def edit(cls):
        pass

    @classmethod
    def delete(cls):
        pass 

if __name__ == "__main__":
    print(ControllerProductsSupplier.display())