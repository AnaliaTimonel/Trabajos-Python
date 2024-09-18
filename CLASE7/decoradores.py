#creando un decorador

def mi_decorador(func):
    def wrapper(*args,**kwargs):
        print("antes de ejecutar la funcion")
        resultado=func(*args,**kwargs)
        print("despues de ejecutar la funcion")
        return resultado
    return wrapper

#usando el decorador en una funcion

@mi_decorador
def saludar(nombre):
    print(f"Hola {nombre}")
saludar("Analia")


 