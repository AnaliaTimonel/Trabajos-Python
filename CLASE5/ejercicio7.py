#Ejercicio 7: Contar Ocurrencias de Elementos en un Diccionario
#Anidado
#1. Crea un diccionario que contenga información sobre tres clubes
#deportivos, cada uno con una lista de jugadores.
#o Cada jugador es un diccionario con las claves: nombre y edad.
#2. Cuenta cuántos jugadores en total tienen cada uno de los clubes


clubes={
    "Club Defensores":{
        "alumnos": 4,
        "primero":{"nombre":"Martin","edad":14},
        "segundo":{"nombre":"Elias","edad":12},
        "tercero":{"nombre":"Martin","edad":14},
        "cuarto":{"nombre":"Elias","edad":12}},
    "Club Armonia":{
        "alumnos":5,
        "primero":{"nombre":"Miguel","edad":10},
        "segundo":{"nombre":"Juan","edad":12},
        "tercero":{"nombre":"Martin","edad":14},
        "cuarto":{"nombre":"Emanuel","edad":12},
        "quinto":{"nombre":"ulises","edad":12}},
    "Club Independiente":{
        "alumnos":3,
        "primero":{"nombre":"Ferran","edad":11},
        "segundo":{"nombre":"Andres","edad":12},
        "tercero":{"nombre":"Maximo","edad":14}}}

alumnos1=clubes["Club Defensores"]["alumnos"]
alumnos2=clubes["Club Armonia"]["alumnos"]
alumnos3=clubes["Club Independiente"]["alumnos"]

print(f"El club Defensores tiene {alumnos1} alumnos")
print(f"El club Armonia tiene {alumnos2} alumnos")
print(f"El club Independiente tiene {alumnos3} alumnos")
