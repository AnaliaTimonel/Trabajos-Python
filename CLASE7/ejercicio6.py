
lista_num=[]
lista_pares=[]
for i in range(1,16):
    lista_num.append(i)
    if i%2==0:
        lista_pares.append(i)
        print("Lista de pares:",i)
    
     
print("Lista normal del 1 al 15:", lista_num)
print("Lista de pares:",lista_pares)
lista_pares_al_cuadrado=[ i**2 for i in range(1,16) if i%2==0]
print("Lista de pares al cuadrado:", lista_pares_al_cuadrado)
    
    
