from cliente import Cliente
def main():
    c1 = Cliente ("Wellington", "Flores", "Rua nao sei o que la", 51900000, "gostosinho@gmail.com", "M")
    if c1._email == "gostosinho@gmail.com":
        print("Email verificado é o gostosinho")
    else:
        print("Email não verificado")    
if __name__ == "__main__":
    main()