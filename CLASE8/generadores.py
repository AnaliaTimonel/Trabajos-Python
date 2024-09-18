def contador():
    #iterra numeros del 1 al 5
    for i in range(1,6):
        yield i  #produce el valor de i y pausa la ejecucion
        
#crear una instancia para el generador

gen= contador() #gen es un objeto generador

#iterar sovbre los valores producidos por el generador

for numero in gen:
    print(numero)#imprime cada uno de los numeros producidos por el generador
    
    
 
def fibonacci():
    print("Primeros 100 numeros Fibonacci")
    a,b=0,1#inicializa los primeron nuemros de la secuencia
    while True:
        yield a #produce el valor de a y causa la ejecucion
        a,b=b, a+b 
    
gen=fibonacci()
for _ in range(100):
        
        print(next(gen)) #obtiene l siguiente numero en la secuencia y lo imprime
        