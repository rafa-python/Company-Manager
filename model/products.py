class Product:
    def __init__(self, name, purchase_price, supplier, stock, category):
        self.name = name 
        self.purchase_price = purchase_price
        self.suplier = supplier
        self.sale_price = self.purchase_price + (self.purchase_price * 0.80)
        self.stock = stock
        self.category = category


class SupplierProduct:
    def __init__(self, name, price, stock, category):
        self.name, self.price, self.stock, self.category = name, price, stock, category
    
    def __str__(self):
        return f'name: {self.name}\nprice: {self.price}\nstock: {self.stock}\ncategory: {self.category}'

if __name__ == "__main__":
    p1 = Product("Copo 150ml", 5, "MG Distri")
    print(p1.sale_price)