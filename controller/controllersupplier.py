import os
import sys
from prettytable import PrettyTable

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from dao.daoclasses import *


class ControllerSupplier:
    @classmethod
    def add(cls):
        print("====================================================")
        cnpj = input("Informe o CNPJ: ")
        response = DaoSupplier.func_check_if_exists(cnpj, "cnpj", "Supplier")

        if response:
            response = "fornecedor ja cadastrado"
        else:
            name = input("Informe o nome: ")
            contact = input("Informe o fone: ")

            response = DaoSupplier.func_add(
                "Supplier", name=name, contact=contact, cnpj=cnpj
            )

        return response

    @classmethod
    def display(cls):
        print("====================================================")
        table = PrettyTable(["ID", "NOME", "CONTATO", "CNPJ"])
        data = DaoClient.get_all("Supplier")
        [table.add_row(row) for row in data]

        return table

    @classmethod
    def edit(cls):
        print("====================================================")
        id = input("Informe o id: ")
        response = DaoSupplier.func_check_if_exists(id, "id", "Supplier")

        if response:
            response = ""
            name = input("Informe o nome: ")
            contact = input("Informe o fone: ")
            cnpj = input("Informe o cnpj: ")

            if name != "":
                DaoSupplier.func_edit("Supplier", id, name=name)
                response += "Nome atualizado\n"

            if contact != "":
                DaoSupplier.func_edit("Supplier", id, contact=contact)
                response += "Contato atualizado\n"

            if cnpj != "":
                DaoSupplier.func_edit("Supplier", id, cnpj=cnpj)
                response += "cnpj atualizado\n"

            if name == "" and contact == "" and cnpj == "":
                response = "nada para atualizar"

        return response

    @classmethod
    def delete(cls):
        print("====================================================")
        id = input("Informe o id: ")
        response = DaoSupplier.func_check_if_exists(id, "id", "Supplier")
        if response:
            DaoSupplier.func_delete(id, "id", "Supplier")
        else:
            return "fornecedor nao encontrado"


if __name__ == "__main__":
    print(ControllerSupplier.display())
