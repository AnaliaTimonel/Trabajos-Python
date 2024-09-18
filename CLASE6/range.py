

for numero in range(5):
    print(numero)
    
    #ejemplo strat, step
print("___")
    
for numero in range(2,6):
    print(numero)


#list comprehension( son una anidacion de bucle FOR CON OPERACIONES Y CONDICIONALES)

print("----")
cuadrado=[x**2 for x in range(5)]
print(cuadrado)

pares=[x for x in range(10) if x%2==0]
print(pares)

