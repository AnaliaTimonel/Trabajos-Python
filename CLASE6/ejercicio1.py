

lista_numeros=[1,2,3,4,4,5,6,7,8,9,9]
lista_a_set=set(lista_numeros)
for i,num in enumerate (lista_a_set):
    print(f"En el puesto {i}: el valor {num}")
    numero_random=4
lista_mayores=[]

for num in lista_a_set:
 if num>numero_random:
  lista_mayores.append(num)
  print(f"Los numeros mayores al numero dado {numero_random} ,son {set(lista_mayores)}")
    
else:
 print("")
    
     




