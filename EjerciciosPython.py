def par_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

numero = int(input("Ingresa el numero para verificar si es par o impar: "))
resultado = par_impar(numero)

print()
print("El", numero, "es", resultado)           




