lista_numeros=[]
numero=None

while numero != 0:
 numero=int(input("Porfavor ingrese un numero (del 0 al 10): "))
 if numero!=0:
     almacenar=lista_numeros.append((numero))
     print("intenta con otro")
     
 else:
     print(f"La lista de numeros es: {lista_numeros}")
     print(f"La suma de los digitos de dicha lista son : {(sum(lista_numeros))}")
     
print("Hasta la proxima!")