def es_palindromo(cadena):
    cadena_limpia = "".join(c for c in cadena if c.isalnum()).lower()
    return cadena_limpia == cadena_limpia[::-1]

def main():
    texto = input("Ingresa una cadena de texto: ")

    if es_palindromo(texto):
        print("Es un palíndromo.")
    else:
        print("No es un palíndromo.")

if __name__ == "__main__":
    main()
