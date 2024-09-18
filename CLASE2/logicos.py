

a=10
b=5
c=15
d=8

resultado_and= (a>b) and (c>d)
print(f"resultado: (a>b) and (c>d): {resultado_and}")
#ambas condiciones deben ser verdades para que de True

resultado_or=(a<b) or (c>d)
print(f"resultado de (a<b) or (c>d): {resultado_or}")
#al menos uan condicion debe ser True


resultado_not= not (a<b)
print(f" {resultado_not}")
#es uan afirmacion negativa como decir que a NO ES MENOR  que b


resultado_conbinado=(a>b) and (not(c<d)) or (b<c)
print(resultado_conbinado)

#(a>b) es true / (not (c<d) es false)= TRUE
#(B<C) ES TRUE.......POR ENDE TRUE + TRUE = TRUE



