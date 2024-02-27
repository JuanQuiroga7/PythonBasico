def multiplicar(numero):
    rango = [numero]
    
    for i in range(2, 11):
        siguiente_numero = rango[-1] + numero
        rango.append(siguiente_numero) 
    return rango

numero = int(input("Ingrese un numero para ver la tabla de multiplicar: "))
rango = multiplicar(numero)

print("Tabla de multiplicar de ",numero)
for i, resultado in enumerate(rango, start=1):
    print(numero, "x", i, "=", resultado)













