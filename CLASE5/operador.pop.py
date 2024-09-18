

diccionario={
    "nombre":"Analia",
    "edad": 32 ,
    "ciudad":"Colon", 
    
      }

eliminar=diccionario.pop("edad")
print(f"valor eliminado, edad: ", eliminar)
print(f"diccionario despues de eliminar el valor edad:", diccionario)


#eliminando un valor no existente
valor_inexistente="pais"

eliminar=diccionario.pop("pais", " valor no especificado")
print(eliminar)

