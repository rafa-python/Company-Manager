from model import products, supplier


if __name__ == '__main__':
    p1 = products.SupplierProduct("Sabao", 3, 100, "limpeza")
    p2 = products.SupplierProduct("Coca-Cola", 5, 50, "Alimentos")
    s1 = supplier.Supplier("MG Distri", '(85)9.888-888', p1, p2)
    print(s1)