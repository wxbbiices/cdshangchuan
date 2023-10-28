import random

ptwo=random.uniform(8,15)
set_ptwo=round(ptwo,1)
pthree=random.uniform(10,16)
set_ptheee=round(pthree,1)
print(set_ptwo)
print(set_ptheee)
if set_ptwo==set_ptheee:
    set_ptheee=set_ptwo+1
    set_ptwo=set_ptwo
print(set_ptwo)
print(set_ptheee)
if set_ptwo>set_ptheee:
    set_ptheee,set_ptwo=set_ptwo,set_ptheee
print(set_ptwo)
print(set_ptheee)



