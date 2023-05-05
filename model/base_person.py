from abc import ABC, abstractmethod 

class PersonBase(ABC):
    def __init__(self, name, cpf):
        self.name, self.cpf = name, cpf

    def __str__(self):
        return f'{"-"*31}= D A D O S ={"-"*31}\n{"="*75}\nName: {self.name} | CPF: {self.cpf}'
    
