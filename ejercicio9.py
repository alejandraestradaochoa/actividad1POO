def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(str(elemento) for elemento in fila))

def main():
    num_filas = int(input("Ingresa el número de filas de la matriz: "))
    num_columnas = int(input("Ingresa el número de columnas de la matriz: "))

    matriz = []
    for i in range(num_filas):
        fila = []
        for j in range(num_columnas):
            elemento = float(input(f"Ingrese el elemento [{i+1}][{j+1}]: "))
            fila.append(elemento)
        matriz.append(fila)

    print("Matriz generada:")
    imprimir_matriz(matriz)

if __name__ == "__main__":
    main()
