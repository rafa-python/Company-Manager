class Supplier:
    def __init__(self, name, contact, *products):
        self.name, self.contact, self.products = name, contact, list(products)

    def __str__(self):
        products_str = "\n".join([f"{p}\n--------------" for p in self.products])
        traits = "=================="
        return f'{traits}\nname: {self.name}\ncontact: {self.contact}\n+++products:+++\n{products_str}\n{traits}'