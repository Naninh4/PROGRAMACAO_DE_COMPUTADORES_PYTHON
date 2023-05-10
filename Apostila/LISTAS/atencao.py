l1 = [1,2,3,4,5,6,7,8,9,10]
l2=l1
# esse tipo de atribuição é como se fosse um link absoluto
print(l1,"\n", l2)
l2[1] = 20
l3 = l1.copy
# e esse um link simbólico
print(l1,"\n", l2)
