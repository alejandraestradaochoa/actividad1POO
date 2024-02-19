def encontrar_maximo_minimo(lista):
    if not lista:
        return None, None

    maximo = lista[0]
    minimo = lista[0]

    for numero in lista:
        if numero > maximo:
            maximo = numero
        if numero < minimo:
            minimo = numero

    return maximo, minimo

def main():
    lista_numeros = []
    num_elementos = int(input("Ingresa el número de elementos en la lista: "))

    for i in range(num_elementos):
        numero = float(input(f"Ingrese el elemento {i+1}: "))
        lista_numeros.append(numero)

    maximo, minimo = encontrar_maximo_minimo(lista_numeros)

    if maximo is None or minimo is None:
        print("La lista está vacía.")
    else:
        print("El número más grande en la lista es:", maximo)
        print("El número más pequeño en la lista es:", minimo)

if __name__ == "__main__":
    main()
