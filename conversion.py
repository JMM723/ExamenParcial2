# CONVERSION DE TIPOS (CASTING): como transformar un dato en otro :D

# CONVERSION IMPLICITA
# Python la hace solo cuando mezclamos tipos compatibles, sin que se lo pidamos xd
print("CONVERSION IMPLICITA")
entero = 10
decimal = 2.5

resultado = entero + decimal   # int + float, Python convierte el int a float solito
print("10 + 2.5 =", resultado)
print("Tipo del resultado:", type(resultado))   # type nos dice de que tipo es el dato :D

verdadero = True
print("True + 5 =", verdadero + 5)   # True vale 1 y False vale 0, como los sellos de Naruto :D

# CONVERSION EXPLICITA
# aqui nosotros le decimos a Python en que tipo queremos el dato
# se usan las funciones int(), float(), str(), bool() y mas xd

# int(): convierte a entero
print("\nint()")
print(int(7.9))        # int NO redondea, solo corta los decimales, como un chasquido de Thanos :-v
print(int("25"))       # un texto con solo numeros se puede pasar a entero
print(int(True))       # True se convierte en 1
print(int("101", 2))   # el segundo dato es la base, aqui lee el texto como binario :D

# float(): convierte a decimal
print("\nfloat()")
print(float(5))        # el 5 se vuelve 5.0
print(float("3.14"))   # texto con punto decimal a float
print(float("2"))      # tambien acepta texto sin punto xd

# str(): convierte a texto
print("\nstr()")
edad = 20
mensaje = "Tengo " + str(edad) + " anios"   # sin str() truena porque no se suma texto con numero :-v
print(mensaje)
print(str(3.5) + " es un texto ahora")
print(str(True))       # True se vuelve el texto "True"

# bool(): convierte a verdadero o falso
# la regla es sencilla: lo vacio o cero es False, todo lo demas es True :D
print("\nbool()")
print(bool(0))         # False
print(bool(1))         # True
print(bool(-5))        # True, cualquier numero distinto de 0 es True
print(bool(""))        # False, texto vacio
print(bool("hola"))    # True, texto con algo
print(bool([]))        # False, lista vacia
print(bool([0]))       # True, la lista tiene un elemento aunque sea un cero xd

# CONVERSION ENTRE COLECCIONES
# tambien podemos cambiar una coleccion en otra :D
print("\nCOLECCIONES")
tupla = (1, 2, 2, 3, 3, 3)

lista = list(tupla)         # tupla a lista, ahora si se puede modificar
print("A lista:", lista)

conjunto = set(tupla)       # tupla a conjunto, se eliminan los repetidos como en el Kage Bunshin xd
print("A conjunto:", conjunto)

nueva_tupla = tuple(lista)  # lista a tupla, queda protegida como el Domain Expansion de Gojo :D
print("A tupla:", nueva_tupla)

letras = list("Konoha")     # un texto a lista separa cada letra
print("Texto a lista:", letras)

pares = [("Gojo", 100), ("Yuji", 70)]
diccionario = dict(pares)   # lista de tuplas a diccionario, cada tupla es clave y valor
print("A diccionario:", diccionario)

# ORD Y CHR
# convierten entre letras y su numero en la tabla ASCII :D
print("\nORD Y CHR")
print(ord("A"))        # ord da el numero de una letra
print(chr(66))         # chr da la letra de un numero
print(chr(ord("A") + 2))   # sumamos 2 al numero de la A y sale la C xd

# CASTING CON INPUT
# input SIEMPRE regresa texto, aunque el usuario escriba un numero :-v
# por eso hay que convertirlo antes de hacer operaciones
print("\nCASTING CON INPUT")
num1 = input("Escribe un numero: ")
num2 = input("Escribe otro numero: ")

print("Sin convertir se pegan como texto:", num1 + num2)   # 5 y 3 dan 53, no 8 xd
print("Convertidos a int se suman bien:", int(num1) + int(num2))

# ERRORES COMUNES
# si el texto no se puede convertir, Python lanza un error llamado ValueError
# con try y except lo atrapamos para que el programa no truene :D
print("\nERRORES COMUNES")
dato = input("Escribe un numero entero: ")

try:
    numero = int(dato)   # aqui intenta la conversion
    print("Conversion exitosa, el doble es", numero * 2)
except ValueError:
    # entra aqui si escribieron letras o decimales, como "hola" o "3.5"
    print("Eso no es un entero valido, ni Gojo lo convierte xd")

# int("3.5") truena aunque tenga forma de numero, hay que pasar primero por float :-v
print("Truco para texto con decimales:", int(float("3.5")))

# EJEMPLO REAL: PROMEDIO DE SENSORES
# los datos llegan como texto, los convertimos y calculamos :D
print("\nEJEMPLO REAL")
lecturas_texto = ["45", "72.5", "90", "60"]   # asi llegan los datos de un archivo o un sensor

suma = 0
for lectura in lecturas_texto:
    suma = suma + float(lectura)   # cada texto se convierte a float antes de sumar

promedio = suma / len(lecturas_texto)
print("Promedio de lecturas:", promedio)

# convertimos el resultado a texto para armar un mensaje, como cuando Jarvis reporta el estado de la armadura :D
reporte = "El promedio fue " + str(round(promedio, 2)) + " grados"
print(reporte)

# convertimos a entero para mostrar sin decimales
print("Promedio sin decimales:", int(promedio))

# resumen rapido
# int() = entero, corta decimales
# float() = decimal
# str() = texto
# bool() = verdadero o falso
# list() tuple() set() dict() = cambian entre colecciones
# input() siempre da texto, hay que convertirlo
# fin del programa, Avengers Assemble :D