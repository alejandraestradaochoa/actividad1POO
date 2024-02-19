def invertir_lista(lista):
    lista.reverse()

def main():
    lista_original = []

    num_elementos = int(input("Ingresa el número de elementos en la lista: "))
    for i in range(num_elementos):
        elemento = input(f"Ingrese el elemento {i+1}: ")
        lista_original.append(elemento)

    print("Lista original:", lista_original)
    invertir_lista(lista_original)
    print("Lista invertida:", lista_original)

if __name__ == "__main__":
    main()
