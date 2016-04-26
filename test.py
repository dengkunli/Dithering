import numpy as np
l1=[1,"world"] 
l2=l1[:]
print(id(l1))
print(id(l2))

l1[0]="world"  
print (l1)
print (l2)
print(id(l1))
print(id(l2))
