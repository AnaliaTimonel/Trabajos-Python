#ejercicio2

edad=int(input("Indique su edad: "))

if edad>=0 and edad<=12:
    categoria="Niño"
elif edad>=13 and edad<=19:
    categoria="Adolescente"
elif edad>=20 and edad<=64:
    categoria="Adulto"
else:
    categoria="Adulto mayor"
    
print(f"usted pertenece a la categoria {categoria}")