# Conversor de temperaturas

print("Conversor de temperaturas")
print("1. Celsius a Fahrenheit")
print("2. Fahrenheit a Celsius")

opcion = input("Elige una opción: ")
temperatura = float(input("Introduce la temperatura: "))

if opcion == "1":
    resultado = temperatura * 9 / 5 + 32
    print("Resultado:", round(resultado, 2), "F")
elif opcion == "2":
    resultado = (temperatura - 32) * 5 / 9
    print("Resultado:", round(resultado, 2), "C")
else:
    print("Opción no válida")