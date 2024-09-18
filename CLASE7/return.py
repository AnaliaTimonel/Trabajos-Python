

#con return

def cuadrado(numero):
    cuenta=numero*numero
    return cuenta
resultado=cuadrado(4)
print(resultado)


#sin return.....tira NONE
def cuadrado(numero):
    cuenta=numero*numero
   
resultado=cuadrado(4)
print(resultado)

#return dentro del condicional

def clasificar(numero):
    if numero >0:
        return "positivo"
    elif numero<0:
        return "negativo"
    else:
        return "cero"
resultado1= clasificar(10)
resultado2= clasificar(-5)
resultado3= clasificar(0)

print("el numero 10 es :", resultado1)
print("el valor -5 es: ", resultado2)
print("el numero 0 es :", resultado3)

