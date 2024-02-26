def numero_mayor(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

num1 = int(input("Profe, ingrese el primer numero: "))
num2 = int(input("Profe, ingrese el segundo numero: "))
num3 = int(input("Profe, ingrese el tercer numero: "))

resultado = numero_mayor(num1, num2, num3)
print("El numero mayor es ", resultado)


