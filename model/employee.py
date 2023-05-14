from base_person import PersonBase


class Employee(PersonBase):
    def __init__(self, name, cpf, salary, office):
        super().__init__(name, cpf)
        self.salary = salary
        self.office = office

    def __str__(self):
        return (
            super().__str__()
            + f'| Salary: {self.salary} | Office: {self.office}\n{"="*75}'
        )


if __name__ == "__main__":
    f1 = Employee("Rafael", "04739383322", 12000, "Programador")
    print(f1)
