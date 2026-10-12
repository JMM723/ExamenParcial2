#numeros

# Exemplos de uso com números
numeros = [12, 7, 19, 24, 8, 31, 6, 15]

suma = sum(numeros)
media = suma / len(numeros)
mayor = max(numeros)
menor = min(numeros)
pares = sum(1 for n in numeros if n % 2 == 0)
impares = sum(1 for n in numeros if n % 2 != 0)

print(f"Números: {numeros}")
print(f"Suma: {suma}")
print(f"Média: {media:.2f}")
print(f"Mayor: {mayor}")
print(f"Menor: {menor}")
print(f"Pares: {pares}")
print(f"Ímpares: {impares}")
#string
texto = "Hola, mundo!"
print(f"Texto: {texto}")
print(f"Longitud: {len(texto)}")
print(f"En mayúsculas: {texto.upper()}")
print(f"En minúsculas: {texto.lower()}")
#booleano
es_verdadero = True
es_falso = False
print(f"Verdadero: {es_verdadero}")
print(f"Falso: {es_falso}")
#none
valor_nulo = None
print(f"Nulo: {valor_nulo}")