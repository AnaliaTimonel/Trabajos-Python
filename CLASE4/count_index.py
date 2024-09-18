

mi_tupla=( "hola",1, 3.14,"pizza",1,60,"pelicula",1)

#count cuenta cuantas veces aparece un valor
#index devuelve en la primera posicion que aparece un valor

buscar=mi_tupla.count(1)
indice=mi_tupla.index(1)
print(f"el valor buscado se repite {buscar} veces en la tupla")
print(f" la posicion del valor es {indice} en la tupla")

buscar_valor=60

if buscar_valor in mi_tupla:
     mi_tupla.count(buscar_valor)
     print(f"el numero se encuentra en la posicion {buscar}")

else:
    print("el valor no se encuentra en la tupla")
    
    

