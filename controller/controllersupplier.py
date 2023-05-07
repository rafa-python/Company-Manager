import os
import sys
from prettytable import PrettyTable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dao.daoclasses import *

class ControllerSupplier:
    @classmethod
    def add(cls):
        print("====================================================")
        cnpj = input("Informe o CNPJ: ")
        response = DaoEmployee.func_check_if_exists(cnpj, "cnpj", "Supplier")
        
        if response:
            response = 'fornecedor ja cadastrado'
        else:
            name = input("Informe o nome: ")
            contact = input("Informe o fone: ")

            response = DaoSupplier.func_add("Supplier", name=name, contact=contact, cnpj=cnpj)
        
        return response

if __name__ == "__main__":
    print(ControllerSupplier.add())