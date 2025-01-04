
def celsius_convert():
    try:
        celsius = float(input("Entrez des degrés celsius: "))
        fahrenheit = celsius * 9 / 5 + 32
        print(f"{celsius} degrés Celsius equivalent à {fahrenheit} degrés fahrenheit")
        return celsius_convert()
    except ValueError:
        print("saisie incorrecte, entrez un nombre: ")
        return celsius_convert()


print(celsius_convert())