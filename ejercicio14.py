def calcular_media(lista):
    if not lista:
        return None

    total_elementos = len(lista)
    suma = sum(lista)
    media = suma / total_elementos
    return media

def main():
    lista_numeros = []

    num_elementos = int(input("Ingresa el número de elementos en la lista: "))
    for i in range(num_elementos):
        numero = float(input(f"Ingrese el elemento {i+1}: "))
        lista_numeros.append(numero)

    media_resultado = calcular_media(lista_numeros)

    if media_resultado is None:
        print("La lista está vacía.")
    else:
        print("La media aritmética es:", media_resultado)

if __name__ == "__main__":
    main()
