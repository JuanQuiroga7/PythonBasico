def fibonacci(numero):
    fibonacci_serie = [0, 1]

    for i in range(2, numero):
        siguiente_numero = fibonacci_serie[-1] + fibonacci_serie[-2]
        fibonacci_serie.append(siguiente_numero)
    
    return fibonacci_serie

numero = int(input("Ingrese la cantidad veces que desea generar la serie Fibonacci: "))

fibonacci_serie = fibonacci(numero)
print()
print("Se genero la serie Fibonacci ", numero," veces. ")
print("El resultado es: ", fibonacci_serie)










