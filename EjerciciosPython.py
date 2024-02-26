def factorial (numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

numero = int(input("Escribe el numero que usaremos: "))
resultado = factorial (numero)

print("El numero factorial de ", numero, "es ", resultado)


