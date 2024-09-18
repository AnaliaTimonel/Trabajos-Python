
print("Lista de nombres enumerados, salteando los comenzados con A y break en CARLOS")
nombres=["Paz","Genaro","Indira","Angel","Analia","Franco","Sandra","Juan","David","Carlos","Cecilia","Pamela"]
print("LISTA ORIGINAL DE NOMBRES:", nombres)

for i, nombre  in enumerate(nombres):
    
    if nombre[0]=="A":
        continue
    if nombre=="Carlos":
          break

    print(f"Posicion {i}: {nombre}")


