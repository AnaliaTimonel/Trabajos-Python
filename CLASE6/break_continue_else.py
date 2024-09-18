
#pedir numero hasta que ingrese un numero negativo

#inicializamos la variable suma para acumular la suma de los numeros positivos ingresados

suma=0

#inicializamos un ciclo infinito usando while true

while True:
    #solicitamos al usuario que introduzca un numero
    #la entrada se convierte en numero entero
    
    entrada=int(input("Ingrese un numero( negativo para terminar): "))
    
    #verificamos si el numero ingresado es negativo
    
    
    #sumamos el numero positivo ingresado a la variable suma
    suma += entrada
    
    if entrada <0:
        #si el numero es negativo salimos del ciclo con el break
        break
    #verificar si el numero ingresado es par
    
    if entrada%2==0:
        #si el numero es par usamos continue para saltar la impresion 
        #y pasar a la siguiente iteracion del siclo
        continue
    
   
    
    #si el numero ingresado no es par , se ejecuta esta linea: 
    print(f"numero inpar ingresado:{entrada}")
    
else:
    print("el bucle finaliza porque el numero es negativo")
     
print(f"la suma de los numeros positivos ingresados da : {suma}")