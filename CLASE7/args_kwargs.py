

#funcion que usa args

def sumar_numeros(*args):
    total=0
    for numero in args:
        total+=numero  
        return total
print(f"suma de 1 , 2 , 3: ",{sumar_numeros(1,2,3)})


def mostrar_detalles(**kwargs):   
    for clave , valor in kwargs.items():
        print(f"{clave} : {valor}")
        
mostrar_detalles(nombre="Ana",edad=36,ciudad= "colon")

def mostrar_info_completa(*args, **kwargs):
    print("Argumentos no nombrados: ")
    for arg in args:
        print(args)
    print("\nArgumentos nombrados: ")
    for clave, valor in kwargs.items():
        print(f"{clave} : {valor}")
print("Ejemplo 3 - Combinados")
mostrar_info_completa(1,2,3,nombre="Ana", edad=30, ciudad="Madrid" )