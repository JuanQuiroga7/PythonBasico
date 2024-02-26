def numero_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0: 
            return False
        return True


numero = int(input("Ingrese el numero para verificar si es primo :D --> "))

print()
if numero_primo(numero):
    print("El numero ", numero, "es primo!! ")
else:
    print("El numero ", numero , "no es primo")



