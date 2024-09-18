
#acceso a la sublista(slicing)


mi_lista=["a","b","c","d","e"]
primer_elemento=mi_lista[0]
segundo_elemento=mi_lista[1]
print(f"segundo elemento: {segundo_elemento}")
print(f"primer elemento: {primer_elemento}")


ultimo_elemento=mi_lista[-1]
penultimo_elemento= mi_lista[-2]
print(f"ultimo elemento: {ultimo_elemento}")
print(f"penultimo elemento: {penultimo_elemento}")

print("sublista (1 al 3):", mi_lista[1:4])
print("sublista del inicio al 3:", mi_lista[:3])
print("sublista del 2 al final:", mi_lista[2:])

#acceso con paso en slicing

print("sublista con paso 2:", mi_lista[::2])
print("sublista con paso en rango (1 al 4):", mi_lista[1:4:2])#----> del indice 1 al 4, salteando de a 2

#iteracion a travez de una lista
for elemento in mi_lista:
   print(elemento)
   
   
