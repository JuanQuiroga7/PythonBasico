panaderia_dulce = {
    "PROMOCION: 2 tortas de manzana": 8000,
    "PROMOCION: 3 donas de fresa": 5000,
    "Pastel de chocolate": 5000,
    "Dona de fresa": 2000,
    "Croissant de almendra": 3000,
    "Torta de manzana": 4500,
    "Bollo de canela": 2500,
    "Galletas de mantequilla": 1800,
    "Torta de zanahoria": 4800,
    "Pera": 1500,
    "Pastel de vainilla": 2200,
    "Red valvet": 3500
}
bebidas_calientes = {
    "PROMOCION: 2 capuchino": 6000,
    "PROMOCION: 2 Café americano": 4000,
    "Café americano": 2500,
    "Café con leche": 3000,
    "Espresso": 2000,
    "Capuchino": 3500,
    "Chocolate caliente": 2800,
    "Té negro": 2200,
    "Té verde": 2300,
    "Té de hierbas": 2400,
    "Mocaccino": 3800,
    "Latte macchiato": 3200
}
panaderia_local = {
     "PROMOCION: 5 pandebonos": 8000,
    "PROMOCION: 2 Pan de bono": 3000,
    "Pandebono": 2000,
    "Almojábana": 1800,
    "Arepa de choclo": 2500,
    "Bollo de mazorca": 2200,
    "Rosca de arequipe": 2800,
    "Bollo de yuca": 2300,
    "Buñuelo": 1500,
    "Arepas de queso": 2100,
    "Pan de bono": 1900,
    "Arequipe con queso": 2600
}
productos_por_categoria = {
    "Pasteleria": panaderia_dulce,
    "Bebidas": bebidas_calientes,
    "Panaderia": panaderia_local
    
}

#BIENVENIDA
print("Bienvenido a Juancho pan :D")
print()
#MENU
print("Menu de seleccion de productos")
for i,categoria in enumerate(productos_por_categoria):
    print(f" {i+1}. {categoria}")

print()
opcion_categoria = int(input("Segun la lista, escriba el numero que corresponde a la categoria: "))

categoria_seleccionada = list(productos_por_categoria.keys())[opcion_categoria - 1]
productos_de_categoria_seleccionada = productos_por_categoria[categoria_seleccionada]

print(f"\nProductos disponibles en la categoría {categoria_seleccionada}:")
for i, (producto, precio) in enumerate(productos_de_categoria_seleccionada.items(), start=1):
    print(f" {i}. {producto} - ${precio}")

opciones_productos = int(input("\nSeleccione el número del producto que desea comprar: "))

producto_seleccionado = list(productos_de_categoria_seleccionada.keys())[opciones_productos - 1]
precio_producto_seleccionado = productos_de_categoria_seleccionada[producto_seleccionado]

print(f"\nVa a realizar la compra de {producto_seleccionado} con un precio de ${precio_producto_seleccionado} pesos.")

dinero= int(input("Ingrese la cantida de dinero disponible: "))
vueltos = dinero - precio_producto_seleccionado

if dinero >= precios[opcion]:
    print(f"Usuario, usted selecciono el producto {productos[opcion]} con un valor de ${precios[opcion]}, sus vueltos son ${vueltos}")
else:
    print(f"El producto que desea comprar {productos[opcion]} con un valor de ${precios[opcion]}, supera el precio de su prespuesto en ${-vueltos}")
