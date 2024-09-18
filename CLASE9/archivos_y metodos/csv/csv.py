import csv

with open ("archivo.csv","r") as file:
    
    reader= csv.reader(file)
    #imprimir cada linea en forma de lista
    for file in reader:
        print(file)