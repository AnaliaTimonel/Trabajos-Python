

lista=[]
lista_inpares=[]
lista_inpares_al_cuadrado=[]
for i in range(1,11):
   
    if i%2==0:
        lista.append(i)
       
        
    else:
       i*2
       lista_inpares.append(i)
       lista_inpares_al_cuadrado.append(i*2)
       
print("lista de numeros pares:", lista)
print(f"Numeros inpares: {lista_inpares}.Lista de inpatres al cuadrado: { lista_inpares_al_cuadrado}")
        
    