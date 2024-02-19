import math

def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    return area

radio_ingresado = float(input("Ingresa el radio del círculo: "))
area_circulo = calcular_area_circulo(radio_ingresado)
print("El área del círculo es:", area_circulo)
