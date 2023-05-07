import os
import sys
from prettytable import PrettyTable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dao.daoclasses import *

class ControllerEmployee:
    @classmethod
    def add(cls):
        print("====================================================")
        cpf = input("Informe o cpf: ")
        
        response = DaoEmployee.func_check_if_exists(cpf, "cpf", "Employee")

        if response:
            response = 'Funcionario ja cadastrado.'

        else:
            name = input("Informe o nome do funcionario: ")
            salary = input("informe o salario: ")
            office = input("Informe o cargo: ")

            response = DaoEmployee.func_add("Employee", name=name, cpf=cpf, salary=salary, office=office)

        return response
    
    @classmethod
    def display(cls):
        print("====================================================")
        table = PrettyTable(["ID", "NOME", "CPF", "SALARIO", "CARGO"])
        data = DaoClient.get_all("Employee")
        [table.add_row(row) for row in data]

        return table
    
    @classmethod
    def edit(cls):
        id = input("Informe o ID: ")
        id_or_none = DaoClient.func_check_if_exists(id, "id", "Employee")
        if id_or_none:
            name = input("Digite o nome ou enter para permanecer com o nome: ")
            cpf = input("Digite o cpf ou enter para permanecer com o cpf: ")
            salary = input("Digite o salario ou enter para permanecer com o salario: ")
            office = input("Digite o cargo ou enter para permanecer com o cargo: ")
            inactive = input("Digite 0 para inativar ou enter para permanecer ativo: ")
            response = ""
            
            if name != "":
                DaoEmployee.func_edit("Employee", id, name=name)
                response += 'Nome atualizado com sucesso.\n'

            if cpf != "":
                DaoEmployee.func_edit("Employee", id, cpf=cpf)
                response += 'cpf atualizado com sucesso.\n'
            
            if salary != "":
                DaoEmployee.func_edit("Employee", id, salary=salary)
                response += 'Salario atualizado com sucesso.\n'
            
            if office != "":
                DaoEmployee.func_edit("Employee", id, office=office)
                response += 'Cargo atualizado com sucesso.\n'
            
            if inactive != "":
                DaoEmployee.func_edit("Employee", id, inactive=inactive)
                response += 'Funcionario inativado com sucesso.\n'
            
            if name == "" and cpf == "" and salary == "" and office == "" and inactive == "":
                response = "Nada para atualizar."
            
        else:
            response = "ID nao encontrado"
        
        return response
    
    @classmethod
    def delete(cls):
        id = input("Informe o ID: ")
        id_or_none = id_or_none = DaoClient.func_check_if_exists(id, "id", "Employee")

        if id_or_none:
            return DaoEmployee.func_delete(id, "id", "Employee")
        
        else:
            return "Funcionario não encontrado."
        
if __name__ == "__main__":
    pass
