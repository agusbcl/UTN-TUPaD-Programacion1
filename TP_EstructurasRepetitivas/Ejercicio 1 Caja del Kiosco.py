# Ejercicio 1— “Caja del Kiosco” 

cliente = input("Ingrese nombre del cliente: ")
while not cliente.isalpha():
    cliente = input("El valor ingresado no es un nombre valido. Ingrese solo letras: ")

productos_str = input("Ingrese cantidad de productos a comprar: ")
while not productos_str.isdigit() or int(productos_str) <= 0:
    productos_str = input("Error, ingrese un numero entero positivo: ")
productos = int(productos_str)

totalSinDescuento = 0
totalConDescuento = 0
listaProductos = []

for i in range(productos):
    precio_str = input(f"Ingrese el precio del producto {i + 1}: ")
    while not precio_str.isdigit() or int(precio_str) <= 0:
        precio_str = input("Ingrese un precio valido: ")
    precio = int(precio_str)
     
    descuento = input("Tiene descuento? S/N: ")
    while descuento.lower() not in ["s", "n"]:
        descuento = input("Ingrese S si tiene descuento o N si no lo tiene: ")

    listaProductos.append(f"producto {i+1}, precio: {precio}, descuento: {descuento.lower()}" )

    totalSinDescuento += precio
    if descuento.lower() == "s":
         totalConDescuento += precio * 0.9
    else:
         totalConDescuento += precio

print(f"\nCliente: {cliente}")
print(f"Cantidad de productos: {productos}")
for p in listaProductos:
    print(p)
print(f"Total sin descuentos: {totalSinDescuento}")
print(f"Total con descuentos: {totalConDescuento:.2f}")
print(f"Ahorro total: {totalSinDescuento - totalConDescuento:.2f}")
print(f"Promedio por producto: {totalConDescuento / productos:.2f}")