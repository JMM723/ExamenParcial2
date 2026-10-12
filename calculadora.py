nombre = input("Ingresa tu nombre: ")
#q mi ex que?

calificaciones = [4]

calificaciones.append(float(input("Ingresa la calificacion 1: ")))
calificaciones.append(float(input("Ingresa la calificacion 2: ")))
calificaciones.append(float(input("Ingresa la calificacion 3: ")))

promedio = sum(calificaciones) / len(calificaciones)

print("===RESULTADO===")
print("Nombre:", nombre)
print("Calificacion 1:", calificaciones[0])
print("Calificacion 2:", calificaciones[1])
print("Calificacion 3:", calificaciones[2])
print("Promedio:", promedio)

if promedio >= 60.0:
    print("Aprobado")
    #gg bro
else:
    print("Reprobado")
    #que wey reprobaste