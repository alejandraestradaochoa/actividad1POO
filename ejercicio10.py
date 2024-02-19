def calcular_factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

numero_ingresado = int(input("Ingresa un número para calcular su factorial: "))
factorial_resultado = calcular_factorial(numero_ingresado)
print(f"El factorial de {numero_ingresado} es: {factorial_resultado}")
