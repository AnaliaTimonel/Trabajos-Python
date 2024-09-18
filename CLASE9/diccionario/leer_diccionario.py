import csv
with open("diccionario.csv","r") as file:
    
    reader= csv. reader (file)
    
    for fila in reader:
        print(fila)
        
            
        
        