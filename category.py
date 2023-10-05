class Category:
    
    def __init__(self, name, description):
        self.name = name
        self.description = description

        cat1 = Category("Esporte", "Equipamentos esportivos")

        cat2 = Category("Alimentos", "Produtos para consumir")

        def Mostrar_informacao() -> None:
            print(cat1.description)
            return description
