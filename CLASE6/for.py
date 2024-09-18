
#sumar los cuadrados de los numeros de una lista

##lista de numeros
numeros=[1,2,3,4,5]

#iniciamos variable

suma_cuadrados=0

#iterar sobre cada nunmero de la lista


for numero in numeros:
    #calcular si el cuadrado del numero
    cuadrado=numero**2
    #imprimir el cuadrado
    print(f"El cuadrado del {numero} es:{cuadrado}")
    suma_cuadrados+= cuadrado
    
    
#imprimir
print(f"La suma de los cuadrados es : {suma_cuadrados}")
    


