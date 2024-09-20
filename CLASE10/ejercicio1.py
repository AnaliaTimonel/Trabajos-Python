
class Estudiantes:
    def __init__(self,nombre,edad,nota):
        self.nombre=nombre
        self.edad=edad
        self.nota=nota
        
        
        if nota>=7:
          print(f"El alumno {nombre} tiene Nota aprobada. Nota: {nota}")
          aprobados.append(nota)
          
        else:
            print(f"El alumno {nombre} tiene Nota desaprobada. Nota: {nota}")

       
aprobados=[]
estudiante1=Estudiantes("Angel",12,9)
estudiante2=Estudiantes("Indira",8,10)
estudiante3=Estudiantes("Genaro",9,9)
estudiante4=Estudiantes("Analia",11,6)
print("Notas aprobadas:", aprobados)



        


            
   
     

     