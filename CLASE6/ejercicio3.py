
#3. Ejercicio con range, enumerate, y break/continue
#Escribe un programa que:
#1. Itere sobre una lista de cadenas usando enumerate para mostrar el
#índice y el valor.
#2. Utilice continue para saltar cadenas vacías.
#3. Utilice break para detener la iteración si se encuentra una cadena
#con más de 5 caracteres

lista=["esmeralda","amatista","turmalina"," ","agata","cuarzo","caliza"]

for i,x in enumerate(lista):
    print(f"{i} : {x}")
       continue x= " "
    