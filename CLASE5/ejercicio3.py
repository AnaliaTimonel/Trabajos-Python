
#Ejercicio 3: Anidación Básica de Diccionarios
#1. Crea un diccionario que represente una persona con las siguientes
#claves:
#o Nombre
#o Edad
#o Dirección (donde la dirección es otro diccionario con claves:
#Calle, Ciudad, Código postal)
#2. Imprime la ciudad de la dirección.

Analia_Timonel={
    "nombre": "Analia",
    "edad":36,
    "direccion":{
        "calle":"tucuman",
        "ciudad":"colon",
        "cp":3280,
    }
}

print("Accediendo a la clave ciudad:", Analia_Timonel["direccion"]["ciudad"])
