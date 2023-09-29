from category import Category

class Product:
    def __init__(self, name, description, date_fabrication, is_active, category) -> None:
        self._name = name
        self._description = description
        self._date_fabrication = date_fabrication
        self._is_active = is_active
        self._category = Category
