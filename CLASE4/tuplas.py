#creat tupla con varios valores

tupla_mixta=(1,"hola", 3.14)
print("tupla mixta: ",tupla_mixta)

#acceder a los elementos de la tupla por indice

print("primer elemento de la tupla: ", tupla_mixta[0])
print("segundo elemento de la tupla: ", tupla_mixta[1])
print("tercero elemento de la tupla: ", tupla_mixta[2])

#tuplas inmutables
print("las tuplas no se pueden modificar")

#explicacion clara de la inmutabilidad
#"si intentamos hacer que trupla_mixta[0]=10, no funcionara porque no se
      #puede modificar los elementos de la tupla ")
      
tupla_mixta= (10,"hola",3.14)
print("volvemos a crear la tupla, pero con el nuevo valor asignado ")

print("la tupla original era: ", tupla_mixta)

#desenpaquetado de tuplas
mi_tupla=(12,"python",1.20)
#desenpaquetamos
numero,texto,flotante=mi_tupla

print("numero:", numero)
print("texto: ", texto)
print("flotante: ", flotante)

#ejemplo, numero de variables no coincide con los elmentos de la tupla

#tira error porque falta otro valor


#desenpaquetado con el operador *

mi_tupla=( "hola",1, 3.14,"pizza",1,"pelicula",1)
primer_elemento,*elresto=mi_tupla

print("primero: ",primer_elemento)
print("el resto:", elresto)


