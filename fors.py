#1. Colecciones: lista, tupla, conjunto y diccionario python
# COLECCIONES: lista, tupla, conjunto y diccionario en un solo programa :D

# LISTA (list)
# se escribe con [] y se puede modificar, ordenada y acepta repetidos
print("LISTA (list)")
heroes = ["Iron Man", "Thor", "Hulk"]

heroes.append("Spider-Man")          # append agrega al final, llego a ultima hora como siempre xd
heroes.insert(1, "Black Widow")      # insert lo mete en la posicion que quieras
heroes.remove("Hulk")                # remove borra por valor, Hulk se fue a otro planeta :-v
print("Lista actual:", heroes)

print("Primero:", heroes[0])         # los indices empiezan en 0
print("Ultimo:", heroes[-1])         # el -1 es un truco para agarrar el ultimo :D
print("Del 1 al 2:", heroes[1:3])    # slicing, el 3 no se incluye xd

heroes.sort()                        # sort ordena alfabeticamente como el ranking de los Hashira :D
print("Ordenada:", heroes)
print("Cuantos son:", len(heroes))

# TUPLA (tuple)
# se escribe con () y NO se puede modificar, como el Domain Expansion de Gojo xd
print("\nTUPLA (tuple)")
coordenadas = (10, 20, 30)

print("Coordenadas:", coordenadas)
print("Primer valor:", coordenadas[0])

# desempaquetar: sacamos cada valor a una variable distinta :D
x, y, z = coordenadas
print(f"x = {x}, y = {y}, z = {z}")

repetida = (1, 2, 2, 3, 2)
print("Cuantos 2 hay:", repetida.count(2))       # count cuenta cuantas veces aparece
print("Posicion del 3:", repetida.index(3))      # index nos dice donde esta

# si intentamos cambiar un valor truena, ni con el Sexto Sentido :-v
# coordenadas[0] = 99

# CONJUNTO (set)
# se escribe con {} y NO acepta repetidos ni tiene orden, como los clones unicos del Kage Bunshin :D
print("\nCONJUNTO (set)")
equipo_a = {"Naruto", "Sasuke", "Sakura", "Naruto"}   # el Naruto repetido se ignora xd
print("Equipo A:", equipo_a)

equipo_b = {"Sasuke", "Kakashi", "Sakura"}

equipo_a.add("Kakashi")              # add agrega un elemento
equipo_a.discard("Kakashi")          # discard lo quita y no truena si no existe :D

# operaciones de conjuntos, como en matematicas :D
print("Union (todos):", equipo_a | equipo_b)
print("Interseccion (en ambos):", equipo_a & equipo_b)
print("Diferencia (solo en A):", equipo_a - equipo_b)

# truco muy usado: quitar repetidos de una lista convirtiendola a set y de regreso xd
lecturas = [50, 60, 50, 70, 60, 80]
sin_repetir = list(set(lecturas))
print("Lecturas sin repetir:", sin_repetir)

# DICCIONARIO (dict)
# se escribe con {} y guarda pares clave:valor, como el intercambio equivalente de Fullmetal Alchemist :D
print("\nDICCIONARIO (dict)")
poder = {"Gojo": 100, "Sukuna": 100, "Yuji": 70}

print("Poder de Yuji:", poder["Yuji"])         # se accede con la clave, no con la posicion
poder["Megumi"] = 65                           # agregar clave nueva
poder["Yuji"] = 75                             # modificar un valor, Yuji entreno xd
print("Con get:", poder.get("Nobara", "No registrada"))   # get evita error si no existe :D

poder.pop("Megumi")                            # pop borra la clave y devuelve su valor :-v
print("Claves:", list(poder.keys()))           # keys da solo las claves
print("Valores:", list(poder.values()))        # values da solo los valores

for nombre, nivel in poder.items():            # items da clave y valor a la vez
    print(f"{nombre} tiene nivel {nivel}")

# COLECCIONES DENTRO DE COLECCIONES
# una lista de diccionarios sirve para guardar muchos registros, como una base de datos pequena :D
print("\nLISTA DE DICCIONARIOS")
sensores = [
    {"nombre": "temperatura", "valor": 45},
    {"nombre": "presion", "valor": 72},
    {"nombre": "humedad", "valor": 90},
]

for s in sensores:
    # cada s es un diccionario, accedemos a sus claves como siempre xd
    if s["valor"] > 80:
        print(f"{s['nombre']}: {s['valor']} Estado critico, Sukuna suelto :-v")
    else:
        print(f"{s['nombre']}: {s['valor']} Todo en orden :D")

# resumen rapido
# lista = ordenada, modificable, con repetidos
# tupla = ordenada, NO modificable
# set = sin orden, sin repetidos
# dict = pares clave y valor
# fin del programa, Avengers Assemble :D
#2. Todos los tipos de for en un solo programa python
# TIPOS DE FOR: todas las formas de usar for en un solo programa :D

# 1. for con range(n)
# repite n veces, empieza en 0 y llega hasta n-1
print("1. range(n)")
for i in range(5):
    print("Vuelta", i)               # como entrenar 5 veces con Gojo :D

# 2. for con range(inicio, fin)
# el fin NO se incluye xd
print("\n2. range(inicio, fin)")
for i in range(1, 6):
    print("Numero", i)               # del 1 al 5, ideal para contar desde 1

# 3. for con range(inicio, fin, paso)
# el paso dice de cuanto en cuanto avanza
print("\n3. range con paso")
for i in range(0, 21, 5):
    print("Voy en", i)               # de 5 en 5 como subir el nivel de poder de Goku :D

print("Cuenta regresiva:")
for i in range(5, 0, -1):            # paso negativo para ir hacia atras
    print(i)
print("Despegue! :D")

# 4. for sobre una lista
# recorre cada elemento directamente, sin necesitar indices
print("\n4. for sobre una lista")
heroes = ["Iron Man", "Thor", "Hulk"]
for heroe in heroes:
    print("Vengador:", heroe)

# 5. for sobre un texto
# un string es una coleccion de letras, asi que tambien se recorre xd
print("\n5. for sobre un string")
for letra in "Konoha":
    print(letra, end=" ")            # end=" " evita el salto de linea
print()                              # print vacio para bajar de linea

# 6. for sobre una tupla
print("\n6. for sobre una tupla")
limites = (50, 80)
for valor in limites:
    print("Limite:", valor)

# 7. for sobre un diccionario
print("\n7. for sobre un diccionario")
poder = {"Gojo": 100, "Yuji": 70, "Megumi": 65}

for nombre in poder:                 # por defecto recorre solo las claves
    print("Hechicero:", nombre)

for nivel in poder.values():         # values recorre solo los valores
    print("Nivel:", nivel)

for nombre, nivel in poder.items():  # items recorre clave y valor a la vez :D
    print(f"{nombre} -> {nivel}")

# 8. for con enumerate
# enumerate nos da el indice y el elemento al mismo tiempo, util cuando queremos numerar xd
print("\n8. enumerate")
for indice, heroe in enumerate(heroes, start=1):   # start=1 para empezar a contar desde 1
    print(f"{indice}. {heroe}")

# 9. for con zip
# zip recorre dos listas en paralelo, como Gojo y Geto siempre en pareja :D
print("\n9. zip")
nombres = ["temperatura", "presion", "humedad"]
valores = [45, 72, 90]
for nombre, valor in zip(nombres, valores):
    print(f"{nombre}: {valor}")

# 10. for con reversed y sorted
print("\n10. reversed y sorted")
for heroe in reversed(heroes):       # reversed recorre al reves sin modificar la lista
    print("Al reves:", heroe)

for valor in sorted(valores, reverse=True):   # sorted ordena sin modificar la lista original :-v
    print("De mayor a menor:", valor)

# 11. for con break
# break corta el ciclo completo, como cuando Light descubre a L y se acaba todo :D
print("\n11. break")
for valor in valores:
    if valor > 70:
        print("Primer valor peligroso:", valor)
        break                        # ya lo encontramos, no hace falta seguir

# 12. for con continue
# continue se salta SOLO esta vuelta y sigue con la siguiente xd
print("\n12. continue")
for i in range(1, 8):
    if i % 2 == 0:
        continue                     # los pares se saltan, como esquivar ataques de Sukuna :-v
    print("Impar:", i)

# 13. for con else
# el else se ejecuta solo si el ciclo termino SIN usar break, es un truco muy poco conocido :D
print("\n13. for con else")
for valor in valores:
    if valor > 100:
        print("Hay un valor imposible")
        break
else:
    print("Ningun valor paso de 100, todo bien xd")

# 14. for anidado
# un for dentro de otro, por cada vuelta del de afuera el de adentro da todas sus vueltas :D
print("\n14. for anidado")
for fila in range(1, 4):
    for columna in range(1, 4):
        print(fila * columna, end="\t")   # \t es un tabulador para acomodar bonito
    print()                               # salto de linea al terminar cada fila

# un patron de estrellas, clasico de la clase de programacion xd
print()
for fila in range(1, 5):
    print("*" * fila)                     # el texto se puede multiplicar :D

# 15. for dentro de una lista (comprehension)
# es un for escrito en una sola linea para crear listas rapido
print("\n15. list comprehension")
cuadrados = [n ** 2 for n in range(1, 6)]
print("Cuadrados:", cuadrados)

criticos = [v for v in valores if v > 70]   # tambien puede llevar un if para filtrar :D
print("Valores criticos:", criticos)

# fin del programa, mision cumplida :D