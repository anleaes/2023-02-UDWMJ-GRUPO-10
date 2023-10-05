from category import Category

class Product:
    def __init__(self, name, description, date_fabrication, is_active, category) -> None:
        self._name = name
        self._description = description
        self._date_fabrication = date_fabrication
        self._is_active = is_active
        self._category = Category

        pd1 = Product ("Arroz", "Arroz baratinho", "16/08/1800", True, Category)
        def mostrarnome ():
            print(pd1._name)