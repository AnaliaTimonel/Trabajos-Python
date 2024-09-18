

#callback simple
def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def operacion(a, b, funcion_callback):
    resultado= funcion_callback (a,b)
    print(f"resultado de la operacion: {resultado}")
    
    