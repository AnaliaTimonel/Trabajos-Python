
lista=[]
mayores_15=set()

for i in range(1,21):
    if i % 3 == 0:
     continue
    lista.append(i)
    if i>15:
        if i%2==0:
         mayores_15.add(i)
    if i>15:
        break
        
print("Numeros, sin divisibles de 3 y break en 15:",lista)
print("Numeros pares de 15 a 20 y no divisibles por 3:", mayores_15)

