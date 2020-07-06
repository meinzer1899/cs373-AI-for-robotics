p = [0.2, 0.2, 0.2, 0.2, 0.2]
world = ['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q = []
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-pHit) * pMiss))
        sumQ = sum(q)
        myList = [x / sumQ for x in q]
    return myList

print(sense(p, Z))
print(sum(sense(p, Z)))
