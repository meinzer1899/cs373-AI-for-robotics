p = [0.2, 0.2, 0.2, 0.2, 0.2]
world = ['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q = []
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-pHit) * pMiss))
    sumQ = sum(q)

    for val in range(len(q)):
        q[val] = q[val]/sumQ

    return q

for entry in measurements:
    p = sense(p, entry)

print(p)
