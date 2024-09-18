

#definimos una funcion, llamamaos con argumentos posicionales

def presentar_persona(nombre,edad,ciudad="desconocido",profesion="desconocido"):
    print("nombre: ",nombre)
    print("edad: ",edad)
    print("ciudad: ", ciudad)
    print("profesion: ", profesion)
    
#distintas formas de llamar a la funcion
#usando argumentos posicionales
print("llamando con argumentos posicionales")
presentar_persona("Ana",36)
    
#llamamos con argumentos posicionales y con nombre

print("ejemplo con argumento posicional y con nombre")
presentar_persona("Paz",27,ciudad="Madrir",profesion="ingeniera")

#usando todos los argumentos con nombres
print("ejemplo de todos los argumentos con nombre")
presentar_persona(nombre="Genaro",edad=29,ciudad="londres",profesion="medico")

