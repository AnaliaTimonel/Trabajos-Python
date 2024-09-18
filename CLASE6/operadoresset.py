

conjunto_a={1,2,3,4}
conjunto_b={3,4,5,6}
conjunto_c={7,8,9}

es_subconjunto=conjunto_a.issubset(conjunto_b)
print("conjunto a es subconjunto de conjunto b?", es_subconjunto)

es_superconjunto=conjunto_b.issuperset(conjunto_a)
print("es conjunto b superconjunto de conjunto a?", es_superconjunto)

#disconjuntos

disconjunto= conjunto_a.isdisjoint(conjunto_c)
print("son disconjuntos conjunto a y conjunto c?", disconjunto)

simetria=conjunto_a.symmetric_difference(conjunto_b)
print(simetria)

union=conjunto_c.update(conjunto_a)
print("es",union)

interseccion=conjunto_a.difference_update(conjunto_b)
print(interseccion)

