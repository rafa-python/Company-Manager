import os
import sys
from prettytable import PrettyTable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dao.daoclasses import *

class ControllerClient:
    
    @classmethod
    def add_client(cls):
        print("====================================================")
        
        cpf = input("informe o cpf do cliente: ")
        response = DaoClient.func_check_if_exists(cpf, "cpf", "Client")
        if response:
            print("Cliente ja possui cadastro")
            print("====================================================")
        else:
            name = input("Informe o nome do cliente: ")
            return DaoClient.func_add("Client", name=name, cpf=cpf)
    
    @classmethod
    def display_client(cls):
        print("====================================================")
        table = PrettyTable(["ID", "NOME", "CPF"])
        data = DaoClient.get_all("Client")
        [table.add_row(row) for row in data]

        return table
    
    @classmethod
    def edit_client(cls):
        response = input("Informe a ID desejado: ")
        id_or_none = DaoClient.func_check_if_exists(response, "id", "Client")
        if id_or_none:
            name = input("Digite o novo nome ou enter para permanecer com o nome: ")
            cpf = input("Digite cpf ou enter para permanecer com o cpf: ")
            inactive = input("Digite 0 para inativar ou enter para permanecer ativo: ")
            result = ""

            if cpf != "":
                DaoClient.func_edit("Client", response, cpf=cpf)
                result += "CPF atualizado\n"

            if name != "":
                DaoClient.func_edit("Client", response, name=name)
                result += "Nome atualizado\n"
            
            if inactive != "":
                DaoClient.func_edit("Client", response, active=inactive)
                result += "Cliente inativado com sucesso"
       
            if name == "" and cpf == "" and inactive == "":
                result = "Nada para atualizar"

        else:
           result= "cliente nao encontrado"
        
        return result

    @classmethod
    def client_delete(cls):
        response = input("Informe a ID desejado: ")
        id_or_none = DaoClient.func_check_if_exists(response, "id", "Client")
        id_client_or_none = DaoClient.func_check_if_exists(response, "id_client", "Sales")

        if id_or_none and id_client_or_none:
            DaoClient.func_delete(response, "id","Client")
            DaoClient.func_delete(id_client_or_none, "id_client", "Sales")
            result = "Cliente e vendas deletadas"
        
        elif id_or_none:
            DaoClient.func_delete(response, "id", "Client")
            result = "Cliente deletado"
        
        else:
            result = "Cliente nao encontrado"
        
        return result


if __name__ == "__main__":
    pass