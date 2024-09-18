#Ejercicio 2: Modificar y Eliminar Elementos de un Diccionario
1.
#Usando el diccionario del ejercicio anterior, actualiza el año de publicación a 1968.
2.
#Elimina el género del diccionario.
3.
#Imprime el diccionario después de cada operación

libro={
    
    "titulo":"orgullo y prejuicio",

    "autor":"Jane Austen",  

    "año":1813,

    "genero":"romanse",

    }


print("Datos del diccionario sin modificar:", libro)

libro["año"]=1968
del libro["genero"]

print("Datos del diccionario eliminando el genero y cambiando el año:", libro)
