import random
print(' 体重  丨  体长  丨  P1')
for i in range(1,200):
    tichang = random.uniform(105, 120)
    tichang=round(tichang,0)
    pone = random.uniform(20, 25)
    pone = round(pone, 1)
    tizhong = random.uniform(110, 140)
    tizhong=round(tizhong, 0)

    print(str(tizhong)+' 丨 '+str(tichang)+' 丨 '+str(pone))