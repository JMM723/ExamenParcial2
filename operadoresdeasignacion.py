# OPERADORES DE ASIGNACION: simulacion de una compra en linea :D

total = 100.0
print("\n=== OPERADORES DE ASIGNACION ===")
print(f"Valor inicial del total: ${total}")   # el f antes de las comillas deja meter variables con {} xd

# += suma y guarda en la misma variable, es igual a total = total + 50
total += 50.0
print(f"Suma $50 de envio (total += 50): ${total}")

# -= resta y guarda, como cuando Thanos le quita la mitad a la lista de compras :-v
total -= 20.0
print(f"Aplica cupon de $20 (total -= 20): ${total}")

# *= multiplica y guarda, como los clones del Kage Bunshin de Naruto :D
total *= 2
print(f"Duplica la orden (total *= 2): ${total}")

# /= divide y guarda, ojo que en Python el resultado siempre sale con decimales xd
total /= 4
print(f"Divide entre 4 personas (total /= 4): ${total}")

# a partir de aqui son los que casi nadie se acuerda :D
print("\n=== MAS OPERADORES ===")

# //= es division entera, tira los decimales como si Light los borrara con el Death Note :-v
total //= 1
print(f"Quitamos los centavos (total //= 1): ${total}")

# %= guarda el residuo de la division, util para saber cuanto sobra xd
total = 47
print(f"\nAhora el total es: ${total}")
total %= 10
print(f"Residuo de repartirlo en grupos de 10 (total %= 10): ${total}")

# **= eleva a una potencia, crece mas rapido que el poder de Goku al transformarse :D
nivel = 3
print(f"\nNivel de poder inicial: {nivel}")
nivel **= 2
print(f"Elevado al cuadrado (nivel **= 2): {nivel}")
nivel **= 2
print(f"Otra vez al cuadrado (nivel **= 2): {nivel}")

# tambien funcionan con texto, += une cadenas, como juntar a los Avengers en una lista :D
equipo = "Iron Man"
print(f"\nEquipo inicial: {equipo}")
equipo += ", Thor"
equipo += ", Hulk"
print(f"Equipo armado (equipo += ...): {equipo}")

# un ejemplo de la vida real, un contador dentro de un ciclo :D
puntos = 0
print("\nGanando puntos por ronda:")
for ronda in range(1, 6):
    puntos += 10   # cada ronda suma 10 puntos xd
    print(f"Ronda {ronda}: {puntos} puntos")

# fin del programa, mision cumplida :D