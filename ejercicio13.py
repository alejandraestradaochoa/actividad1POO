def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división por cero no permitida."

def main():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    resultado_suma = suma(num1, num2)
    resultado_resta = resta(num1, num2)
    resultado_multiplicacion = multiplicacion(num1, num2)
    resultado_division = division(num1, num2)

    print(f"Suma: {resultado_suma}")
    print(f"Resta: {resultado_resta}")
    print(f"Multiplicación: {resultado_multiplicacion}")
    print(f"División: {resultado_division}")

if __name__ == "__main__":
    main()
