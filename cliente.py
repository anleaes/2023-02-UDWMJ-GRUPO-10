class Cliente:
    def __init__(self, first_name, second_name, address, cell_phone, email, gender):
        self._fist_name = first_name
        self._second_name = second_name
        self._address = address
        self._cell_phone = cell_phone
        self._email = email
        self._gender = gender

        c1 = Cliente ("Wellington", "Flores", "Rua nao sei o que la", 51900000, "gostosinho@gmail.com", "M")
        def verificar_email():
            if Cliente._email == "gostosinho@gmail.com":
                print("Email verificado é o gostosinho")
            else:
                print("Email não verificado")
            return 