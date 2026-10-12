# OPERADORES ARITMETICOS: calculadora con dos numeros :D

print(" OPERADORES ARITMETICOS ")

# pedimos los dos numeros, float para aceptar decimales xd
a = float(input("Primer numero: "))
b = float(input("Segundo numero: "))

print("\n=== RESULTADOS ===")

# + suma, como juntar a los Vengadores para sumar fuerzas :D
print(f"Suma ({a} + {b}) = {a + b}")

# - resta
print(f"Resta ({a} - {b}) = {a - b}")

# * multiplicacion, como cuando Naruto hace mas clones :D
print(f"Multiplicacion ({a} * {b}) = {a * b}")

# la division tiene su truco, dividir entre 0 truena el programa, ni Gojo se salva :-v
# por eso primero revisamos que b no sea 0
if b != 0:
    print(f"Division ({a} / {b}) = {a / b}")                        # / da el resultado con decimales
    print(f"Division entera ({a} // {b}) = {a // b}")               # // tira los decimales xd
    print(f"Residuo ({a} % {b}) = {a % b}")                         # % da lo que sobra de la division
else:
    print("No se puede dividir entre 0, hasta Light lo sabe :-v")

# ** es la potencia, a elevado a la b, crece como el poder de Goku :D
print(f"Potencia ({a} ** {b}) = {a ** b}")

# raiz cuadrada con ** 0.5, una potencia a la mitad xd
if a >= 0:
    print(f"Raiz cuadrada de {a} = {a ** 0.5}")
else:
    print("No hay raiz cuadrada real de un numero negativo")

# jerarquia de operaciones, Python respeta el orden como los rangos de los Hashira :D
# primero parentesis, luego potencias, luego * y /, al final + y -
print("\n JERARQUIA DE OPERACIONES ")
print(f"2 + 3 * 4 = {2 + 3 * 4}")          # primero 3 * 4 = 12, luego 2 + 12 = 14
print(f"(2 + 3) * 4 = {(2 + 3) * 4}")      # los parentesis mandan, 5 * 4 = 20 xd
print(f"2 ** 3 ** 2 = {2 ** 3 ** 2}")      # la potencia se resuelve de derecha a izquierda, 3 ** 2 = 9 y luego 2 ** 9 :D

# un ejemplo real, convertir temperatura de Celsius a Fahrenheit :D
print("\n EJEMPLO REAL ")
celsius = float(input("Temperatura del motor en Celsius: "))
fahrenheit = celsius * 9 / 5 + 32   # primero * y /, luego + xd
print(f"{celsius} C equivalen a {fahrenheit} F")

# otro ejemplo, convertir segundos a minutos y segundos usando // y % juntos :D
segundos = int(input("\nTiempo de operacion en segundos: "))
minutos = segundos // 60     # // nos dice cuantos minutos completos hay
resto = segundos % 60        # % nos dice cuantos segundos sobran
print(f"{segundos} segundos son {minutos} min con {resto} seg")

# fin del programa, Avengers Assemble :D