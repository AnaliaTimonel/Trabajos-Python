
#Ejericio 2

#Define una lista de números predefinida.
# Pide al usuario que ingrese el índice de inicio y el índice de fin para
#la sublista.
# Usa slicing para obtener la sublista.
# Suma los elementos de la sublista.
# Muestra la suma.

lista_numeros= [12,18,25,44,54,32,98,70]
i=int(input("ingrese el indice de inicio: "))
f=int(input("Ingrese el indice de fin: "))
sublista= lista_numeros[i:f]
sumar=sum(sublista)
print(f"la lista de numeros es :{lista_numeros}")
print(f"La Sublista seleccionada es: {sublista}")
print(f"El resultado de la suma de los valores de la Sublista es de: {sumar}")