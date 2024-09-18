
persona={
    "nombre":"Analia",
    "Edad":36,
    "Ciudad": "Colon, entre rios"
    
}

valores=persona.values()
print(valores)


valores_lista=list(valores)

print(valores_lista)
clave_ineccistente="pais"

if clave_ineccistente in persona:
    buscar=persona.get(clave_ineccistente)
    print(f"la clave {clave_ineccistente} esta en el diccionario")
else:
    print("la clave no esta en el diccionario")
    
if "nombre" in persona:
    valor= persona["nombre"]
    clave=persona.get("nombre")
   
    print(f"la clave {clave}, existe en el diccionario")
    
else:
    print("la clave no existe en el diccionario")
    
#otro formato

persona_5 = {
    "nombre": "Emilia",
    "edad": 33,
    "ciudad": "CABA"
}
print("nombre" in persona_5)#consultar si una clave esta en un diccionario de forma mas sintactica



