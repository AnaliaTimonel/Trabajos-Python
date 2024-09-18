
#ejemplo diccionario vacio

diccionario_vacio={}
print("ejemplo de un diccionario vacio:", diccionario_vacio)

#diccionario con elementos
diccionario_datos={
    "nombre":"Analia",
    "edad":36,
    "hijos":["Paz","Genaro"],
    "casada": True,
    "direccion":{
        "calle":"tucuman",
        "ciudad":"Colon, Entre Rios",
    }
    }
    
print("Ejemplo de diccionario con contenido:", diccionario_datos)
nombre=diccionario_datos["nombre"]
edad=diccionario_datos["edad"]
print("la edad es:", edad)
print("el nombre es:", nombre)
#ejemplo de diccionario con valores de distintos tipos-mixto, clave es un int, y valor str

diccionario_mixto={
    "nombre":"Alejandra",
    1:[2,3,4],
    2:{2,3,4},
    (2,3,4):3 #tupla puede ser clave porqe es inmutable
    
}
print("esto es un dicciorio mixto:", diccionario_mixto)

# como obtener los elementos en un diccionario      

print(diccionario_datos["hijos"])
print(diccionario_mixto[2])
    
#creamos diccionario

persona={
    
    "Nombre":"Veronica",
    "edad":25,
    "Ciudad":"Buenos Aires",
    
    }
    
#usar el metodo .get para acceder a elementos
nombre=persona.get("nombre")
edad=persona.get("edad")
ciudad=persona.get("ciudad")

print("nombre:", nombre)
print("edad: ", edad)
print("ciudad: ",ciudad)

pais=persona.get("pais ", "no especificado")#en caso de que esa clave no exista, respode automaticamente.
print("pais:", pais)

#acceder a clave que no existe

clave_ineccistente="pais"
if clave_ineccistente in persona:
    valor= persona[clave_ineccistente]
    print(f"la clave es {clave_ineccistente}es:")
else:
    ("la clave no existe")


    
    
    
    
    

    



