def es_par(numero):
    return numero % 2 == 0

def main():
    numero = int(input("Ingresa un número: "))

    if es_par(numero):
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")

if __name__ == "__main__":
    main()
