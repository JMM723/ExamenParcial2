# Conjunto.py
frutas=["manzanas","naranja","naranja","pera"]
print(frutas)
#For.py
for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(6):
    if i == 3:
        continue
    print(i)

#colecciones.py
alumnos = ["Ana","Luis","Paty"]
calif = [9.0,7.5,8.2]

print(alumnos[0])
print(alumnos[-1])

alumnos.append("Carlos")
alumnos.remove("Luis")

print(len(alumnos))

for a in alumnos:
    print(a)


#mi ejemplo
categorias = ["Lácteos", "Panadería", "Lácteos", "Enlatados"]
print(categorias)

for i in range(10):
    if i == 5:
        break
    print(i)

print()

for i in range(6):
    if i == 3:
        continue
    print(i)

print()

productos = ["Pan", "Leche", "Huevos"]
precios = [2.5, 1.8, 3.0]

print(productos[0])
print(productos[-1])

productos.append("Cereal")
productos.remove("Leche")

print(len(productos))

for p in productos:
    print(p)