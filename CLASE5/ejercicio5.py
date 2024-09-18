
producto1={
    "nombre":"azucar",
    "precio":800,
    "stock":96,
}
producto2={
    "nombre":"fideo",
    "precio":1200,
    "stock":72,
}
producto3={
    "nombre":"arroz",
    "precio":1400,
    "stock":48,
}
producto4={
    "nombre":"aceite",
    "precio":1600,
    "stock":60,
}
lista=[]
lista.append(producto1)
lista.append(producto2)
lista.append(producto3)
lista.append(producto4)
nombre=lista[1]["nombre"]
precio=lista[1]["precio"]
print(f"El segundo producto de la lista es {nombre} y vale {precio} pesos")

