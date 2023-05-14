import os
import sys
from prettytable import PrettyTable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dao.daoclasses import *

class ControllerProductsSupplier:
    @classmethod
    def display(cls, table_base, *args):
        print("====================================================")
        print("Table name: ", table_base)
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
    def add(cls):
        print(cls.display("ProductsSupplier", "id", "nome", "valor", "estoque", "categoria", "id fornecedor"))
        id = input("informe o id: ")
        if DaoSupplierProducts.func_check_if_exists(id, "id", "ProductsSupplier"):
            quant = input("informe a quantidade: ")
            response = DaoSupplierProducts.add("ProductsSupplier", id, quant)
        else:
            response = 'Produto nao encontrado'
        
        return response

        

    @classmethod
    def edit(cls):
        print(cls.display("ProductsSupplier", "id", "nome", "valor", "estoque", "categoria", "id fornecedor"))
        id = input("informe o id: ")
        response = ""
        if DaoSupplierProducts.func_check_if_exists(id, "id", "ProductsSupplier"):
            
            nome = input("Informe o nome ou enter para nao atualizar: ")
            valor = input("Valor ou enter para nao atualizar: ")
            stoque = input("Estoque ou enter para nao atualizar: ")
            categoria = input("Categoria ou enter para nao atualizar: ")
            id_fornecedor = input("id do fornecedor: ")
            
            if DaoSupplierProducts.func_check_if_exists(id_fornecedor, "id", "Supplier"):
                if nome != "":
                    DaoSupplierProducts.func_edit("ProductsSupplier", id, name=nome)
                    response += "Nome atualizado\n"

                if valor != "":
                    DaoSupplierProducts.func_edit("ProductsSupplier", id, price=valor)
                    response += "Valor atualizado\n"
                
                if stoque != "":
                    DaoSupplierProducts.func_edit("ProductsSupplier", id, stock=stoque)
                    response += "Estoque atualizado\n"
                
                if categoria != "":
                    DaoSupplierProducts.func_edit("ProductsSupplier", id, category=categoria)
                    response += "Categoria atualizado\n"
                
                if nome == "" and valor == "" and stoque == "" and categoria == "":
                    response = "Nada para atualizar"
                
            else:
                response = "Fornecedor não localizado"
            
        else:
            response = "Produto nao localizado"
        
        return response
                



    @classmethod
    def delete(cls):
        pass 

if __name__ == "__main__":
    print(ControllerProductsSupplier.edit())