
#EJERCICIOS 27/8
#ejercicio 1

# Define una lista de números predefinida o pídele al usuario que
#ingrese los números.
# Pide al usuario que ingrese un número a buscar.
# Usa el método count() para determinar cuántas veces aparece el
#número en la lista.
# Muestra el resultado.

numeros=[2,8,31,36,8,44,12,23,8,28]
buscar=int(input("Ingrese el numero que desea buscar: "))
resultado=numeros.count(buscar)

print(f"El numero {buscar} se encuentra {resultado} de veces en la lista")
