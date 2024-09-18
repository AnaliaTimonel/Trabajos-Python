
empresa={
    "nombre_empresa":"Moon Light",
     "empleados":[
       {"id_empleado":1234,"nombre":"Angel Montañez","departamento":"laboratorio","salario":980000},
       {"id_empleado":1235,"nombre":"Franco Lopez","departamento":"marketing","salario":900000},
       {"id_empleado":1236,"nombre":"Genaro Fernandez","departamento":"laboratorio","salario":980000}]}


for j in range(0,3):
    for i in empresa["empleados"][(j)]:
      print("primera itarcion:", j, i)
    
id=int(input("Ingrese ID:" ))
id_empleado=empresa["empleados"][j][("id_empleado")]
print(id_empleado)
identificar_id="Id encontrado:", {id_empleado} if id==id_empleado else "Id inexistente"
print(f"{identificar_id}")
cambio_salario=empresa["empleados"][0]["salario"]=1200000
usuario=empresa["empleados"][(0)]


usuario=empresa["empleados"][(0)]
print(F"Datos del empleado actualizados, con incremento de salario:{usuario}")
    
    

