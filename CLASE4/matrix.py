
matrix=[
    [1,2,3],#fila 0
    [4,5,6],#fila 1
    [7,8,9]# fila 2
    ]

buscar=matrix[1][1]
print(buscar)

#modificar elementos especificos de la matrix
matrix[0][0]=10
matrix[2][0]=15

print("cambiamos el valor de la fila 0, columna 0, a 10: ", matrix)

#acceder a una fila completa
print("accediendo a la fila completa")
print(matrix[1])


#reemplazando una fila completa
matrix[1]=[20,21,22]
print("matrix despues de reemplazar la fila 1 :", matrix)

#trabajar con submatrix, substraje los valores determinados 
submatrix= matrix[0][1:3], matrix[1][1:3]

print(submatrix)

#mostramos como quedo la matrix al final
print(matrix)