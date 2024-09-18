import csv



fieldsname=["nombre","edad","ciudad"]

with open("esscribirlista.csv","w",newline=" ") as file:
    writer= csv.DictWriter(file,fieldnames= fieldsname)
    
    writer.writeheader()
    
    
    writer.writerow({"nombre":"ana","edad":36})
    
    writer.writerows()