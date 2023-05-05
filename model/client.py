from base_person import PersonBase

class Client(PersonBase):
    def __init__(self, name, cpf):
        self.active = True
        super().__init__(name, cpf)

if __name__ == "__main__":
    p1 = Client("Rafael Matins", '04739383322')
    print(p1)