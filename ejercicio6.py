def calcular_suma(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

def main():
    lista_numeros = []
    num_elementos = int(input("Ingresa el número de elementos en la lista: "))

    for i in range(num_elementos):
        numero = float(input(f"Ingrese el elemento {i+1}: "))
        lista_numeros.append(numero)

    suma_total = calcular_suma(lista_numeros)
    print("La suma de los números en la lista es:", suma_total)

if __name__ == "__main__":
    main()
