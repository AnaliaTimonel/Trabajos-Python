
lista=[1,3,6,8,12,14,15,18,20]
mayores_10=[]
divisible_15=[]
numeros_sin_condicion=[i for i in lista if i<=10 or i%15==1]

for i in lista:
    if i>=10:
        mayores_10.append(i)
        continue
    
    if i%15==0:
        divisible_15.append(i)
        break
       

    
print("Lista normal:", lista)
print("lista con mayores de 10:",mayores_10)
print("break en numero divisible por 15:", divisible_15)
print("Numero que no cumplen condicionales:", numeros_sin_condicion)
