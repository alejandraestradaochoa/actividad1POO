def obtener_numeros_pares(inicio, fin):
    lista_pares = [numero for numero in range(inicio, fin + 1) if numero % 2 == 0]
    return lista_pares

numeros_pares = obtener_numeros_pares(1, 100)

print("Lista de números pares entre 1 y 100:")
print(numeros_pares)
