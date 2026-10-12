# EJERCICIO 1 LISTAS: registro de temperaturas de un motor :D

# lista vacia que crece sola como los clones del Kage Bunshin de Naruto :D
temperaturas = []

# pedimos cuantas lecturas y repetimos hasta que sea mayor a 0
cantidad = 0
while cantidad < 1:
    cantidad = int(input("Cuantas lecturas quieres registrar: "))
    if cantidad < 1:
        print("Tiene que ser al menos 1 xd")

# ciclo for para llenar la lista, como juntar las Esferas del Dragon una por una :D
for i in range(cantidad):
    temp = float(input("Temperatura " + str(i + 1) + " (C): "))
    temperaturas.append(temp)   # append agrega al final, como cuando llega Spider-Man a ultima hora xd

# mostramos todas las lecturas
print("\nLecturas:", temperaturas)

# calculos basicos con funciones que ya trae Python :D
promedio = sum(temperaturas) / len(temperaturas)   # sum suma todo y len cuenta cuantos hay
maxima = max(temperaturas)                         # max encuentra la que tiene mas poder xd
minima = min(temperaturas)                         # min encuentra la mas debil

print("Promedio:", promedio)
print("Maxima:", maxima)
print("Minima:", minima)

# contamos cuantas lecturas pasan el limite de seguridad, como detectar maldiciones de grado especial en JJK :-v
limite = 80
peligrosas = 0   # contador que empieza en 0
for t in temperaturas:
    if t > limite:
        peligrosas = peligrosas + 1   # sumamos 1 cada vez que una lectura se pasa

print("Lecturas arriba de", limite, "grados:", peligrosas)

# sort ordena de menor a mayor, como el ranking de los Hashira de Demon Slayer :D
temperaturas.sort()
print("Ordenadas de menor a mayor:", temperaturas)

# pop saca el ultimo, que despues de ordenar es el mas alto
mayor = temperaturas.pop()   # un chasquido de Thanos pero solo a uno :-v
print("Quitamos la lectura mas alta:", mayor)
print("Lista final:", temperaturas)

# fin del programa, mision cumplida :D