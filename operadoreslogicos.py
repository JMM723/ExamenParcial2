precio_producto = 150.0
cantidad = 3
costo_envio = 50.0
descuento = 20.0

suma = precio_producto + costo_envio
resta = precio_producto - descuento
multiplicacion = precio_producto * cantidad
division = precio_producto / 2
potencia = 2 ** 3
division_entera = 10 // 3
modulo = 10 % 3

print("\n--- OPERADORES ARITMÉTICOS ---")
print(f"Total compra (3 productos): ${multiplicacion}")
print(f"Precio con descuento: ${resta}")
print(f"Precio con envío incluido: ${suma}")
print(f"Mitad del precio: ${division}")
print(f"Residuo de 10 / 3: {modulo}")