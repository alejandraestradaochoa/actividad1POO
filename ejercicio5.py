def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Ejemplo de uso
temperatura_fahrenheit = float(input("Ingresa la temperatura en grados Fahrenheit: "))
temperatura_celsius = fahrenheit_a_celsius(temperatura_fahrenheit)
print(f"{temperatura_fahrenheit} °F equivale a {temperatura_celsius:.2f} °C")
