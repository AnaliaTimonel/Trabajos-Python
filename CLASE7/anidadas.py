

#funciones anidadad

def funcion_externa(x):
    def funcion_interna(y):
        return y + 10
    return funcion_interna(x)
resultado= funcion_externa(5)
print(f" Suma de dos funciones anidadas:", resultado)
    



#closure

def crear_multiplicadores(factor):
    def multiplicar(x):
        return x* factor
    return multiplicar
dupli=crear_multiplicadores(2)
triplicar= crear_multiplicadores(3)

print(f"multiplicar el 10: ",dupli(10))
print(f" triplicar el 10; ", triplicar(10))