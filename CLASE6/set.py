
#gestion de asistentes a un evento
#crear un programa que administre una lista de asistentes a eventos
#sin permitir publicados y que realice operaciones entre dos listas

#crear sets de invitados

invitados_viernes={"Ana","carlos","pedro","maria","julia"}
invitados_sabado={"sofia","luis","pedro","elena","maria"}

#invitados unicos del viernes

print("Invitados del viernes:", invitados_viernes)
print("Invitados del sabado:", invitados_sabado)

#union de ambos sets de invitados, quien asistio al menos un dia
todos_asistentes=invitados_sabado|invitados_viernes
print("Asistentes de ambos dias:", todos_asistentes)

#mostrar la la interseccion (quien asistio ambos dias)los repetidos
ambos_dias= invitados_viernes&invitados_sabado
print("Asistieron solo un dia:",ambos_dias)

invitados_vier= invitados_viernes-invitados_sabado
print("asistencia solo el viernes:",invitados_vier)

#agregar in invitado

invitados_viernes.add("paz")
print("agregar invitado:", invitados_viernes)
#eliminar un invitado
invitados_sabado.remove("elena")
print("invitados del sabado, despues de eliminar un invitado:",invitados_sabado)

#comprovar si un invitaso assistio el sabado
print("sofia asistio el sabado?","ana" in invitados_sabado)