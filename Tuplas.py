# EJERCICIO 2 TUPLAS: clasificacion de sensores con limites fijos :D

# los limites no deben cambiar nunca, asi que van en una tupla
# es como el Domain Expansion de Gojo, una vez activado no se modifica xd
LIMITES = (50, 80)

# desempaquetamos la tupla en dos variables :D
bajo, alto = LIMITES

# lista donde cada elemento es una tupla (nombre, valor), siempre en pareja como Gojo y Geto :D
sensores = []

cantidad = int(input("Cuantos sensores vas a registrar: "))

# llenamos la lista con tuplas, como armar el equipo de los Vengadores uno por uno :D
for i in range(cantidad):
    nombre = input("Nombre del sensor " + str(i + 1) + ": ")
    valor = float(input("Valor de " + nombre + ": "))

    # los dobles parentesis son porque agregamos una tupla completa a la lista
    sensores.append((nombre, valor))

# recorremos la lista desempaquetando cada tupla en nombre y valor
print("\n===== RESULTADOS =====")
for nombre, valor in sensores:
    if valor < bajo:
        estado = "Estado normal"           # todo tranquilo, dia normal en Konoha :D
    elif valor <= alto:
        estado = "Requiere supervision"    # hay que vigilarlo, como a Loki xd
    else:
        estado = "Estado critico"          # Sukuna suelto, a correr :-v

    print(nombre, "->", valor, ":", estado)

# funcion que regresa DOS valores, Python los entrega como una tupla :D
def mayor_y_menor(datos):
    valores = []
    for nombre, valor in datos:
        valores.append(valor)   # sacamos solo los valores de cada tupla
    return max(valores), min(valores)

# recibimos la tupla que regresa la funcion y la desempaquetamos xd
mayor, menor = mayor_y_menor(sensores)
print("\nValor mas alto:", mayor)
print("Valor mas bajo:", menor)

# si intentamos cambiar los limites truena porque las tuplas son inmutables, ni con el Sexto Sentido :-v
# LIMITES[0] = 60