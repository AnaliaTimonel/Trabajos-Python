
alumno1={
    "nombre":"Genaro",
    "edad":12,
    "calificacion":[9,7,8,10]
       }
alumno2={
    "nombre":"Indira",
    "edad":13,
    "calificacion":[10,9,8,9]
        }
alumno3={
    "nombre":"Angel",
    "edad":13,
    "calificacion":[9,8,7,8]
        }
lista=[]
lista.append(alumno1)
lista.append(alumno2)
lista.append(alumno3)

nombre=lista[0]["nombre"]
calificaciones=lista[0]["calificacion"]

print("El nombre del alumno es:", nombre ,".  Sus calificaciones son:", calificaciones)
