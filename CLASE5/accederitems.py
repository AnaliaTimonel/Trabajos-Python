persona={
    
    "nombre":"Alejandra",
    "edad":30,
    "ciudad": "merida"
}

pares_clave_valor=persona.items()
print("pares_clave_valor:",pares_clave_valor)
      
valores_lista=list(pares_clave_valor)#lo organizamos en lista

print(valores_lista)

#comprobar existencia de clave en diccionario, antes de acceder a su valor

clave="edad"

if clave in persona:
    valor=persona[clave]
    print(f"el valor de {clave} es :", valor)
else:
    print(f"la clave {clave} no existe en el diccionario")
    
    
    
edades = {'Juan': 30, 'María': 25, 'Pedro': 35, 'Luisa': 28}

# Obtener una vista de los valores en el diccionario
valores = edades.values()

# Mostrar los valores
for edad in valores:
 print(edad)
