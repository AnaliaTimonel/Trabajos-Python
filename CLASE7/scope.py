

#scope es el alcance que tiene una variable
x=20#variable global


def funcion_local():
    x=10#variable local
    print(f"El valor de x dentro de la funcion local vale {x}")
funcion_local()

def funcion_global():
   # global x #para modificar la variable global
    x=30
    print(f"el valor de x dentro d ela cuncion global es {x}")
    
funcion_global()

print(f"el valor de x fuera de la funcion vale {x}")