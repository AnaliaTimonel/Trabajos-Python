

#adivinar el numero secreto

numero_secreto=7

#iniciamos la variable para almacenar el numero del usuario
numero_adivinado=None

#mensaje Inicial
print("Adivina el numero secreto (entre el 1 y el 10!!!)")


#bucle que continua hasta que el usuario adivine el numero secreto

while numero_adivinado!=numero_secreto:
    #solicitamos ingresar un numero al usuario
    numero_adivinado=int(input("Introduzca un numero:" ))
    if numero_adivinado<numero_secreto:
        print("demasiado bajo, intenta de nuevo")
    elif numero_adivinado>numero_secreto:
        print("el numero es muy alto, vuelve a intentarlo")
    else:
        print("Muy bien has adivinado el numero secreto:", numero_secreto)
        
        
        
print("Gracias por jugar!!!")
    


