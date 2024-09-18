
precio=500
descuento=precio*15/100
total=precio-descuento
 
if precio>200:
    print(f"El monto a pagar es de $ {precio}. Usted aplica al descuento")
    print(f"Su descuento es de {descuento}")
    print (f"Usted pagara {precio-descuento} en total")
     
     
else:
    print("usted no aplica al decuento")
