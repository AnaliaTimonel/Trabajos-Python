#lambda
suma=lambda x,y: x+y
print(f"suma de 5 y 3:  {suma(5,3)}")

numeros=[1,2,3,4,5]
cuadrados= lambda x,y: x*y,numeros
print (f"el cuadrado de la lista :,{numeros} :{list(cuadrados)}")


#lambda usando map

numeros=[1,2,3,4,5]
cuadrados=map(lambda x:x**2, numeros)
print(f" Cuadrados de la lista: {numeros}:{list(cuadrados)}")

#usando filter

numeros=[1,2,3,4,5,6]
pares=filter(lambda x: x%2==0, numeros)
print(f"pares de la lista {numeros}:{list(pares)}")

#usando sorted

tuplas=[(1,5),(3,1),(5,2)]
ordenar=sorted(tuplas, key=lambda t:t[1] )
print("ordenar la tupla por su segundo elemento:", ordenar)

#usando reduce
