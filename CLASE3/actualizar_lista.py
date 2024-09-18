
mi_lista=[10,20,30,40,50]
print("lista original: ", mi_lista)

#actualizar un elemento especifico
mi_lista[2]=35
print("lista actualizada: ", mi_lista)

mi_lista[-1]=55
print("mi lista:", mi_lista)

#actualizar elementos utilizando slicing

mi_lista[1:4]=25,33,45,69

print("actualizando elelemntos de la lista:" , mi_lista)

#actualizar basado en una condicion, en este caso le sumamos 10
# a todos los numeros mayores de 30

for i in range(len(mi_lista)):
    if mi_lista[i]>30:
        mi_lista[i]+=10
print("actuaslizar elementos mayores de 30: ", mi_lista)