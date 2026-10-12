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