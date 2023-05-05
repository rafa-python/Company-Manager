import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controller.controllerclient import ControllerClient
class ViewClient:
    
    @classmethod
    def menu(cls):
        print("==Cliente==")
        print("1 - Para cadastrar novo cliente")
        print("2 - Exibir clientes cadastrados")
        print("3 - Atualizar cliente")
        print("4 - Deletar cliente")
        print("5 - retornar ao menu principal")
        choice = int(input("Digite a opção desejada: "))

        if choice == 1:
            print(ControllerClient.add_client())
        
        elif choice == 2:
            print(ControllerClient.display_client())
        
        elif choice == 3:
            print(ControllerClient.display_client())
            print(ControllerClient.edit_client())
        
        elif choice == 4:
            print(ControllerClient.display_client())
            print(ControllerClient.client_delete())

        elif choice == 5:
            # menu principal
            pass
            

if __name__ == "__main__":
    ViewClient.menu()
