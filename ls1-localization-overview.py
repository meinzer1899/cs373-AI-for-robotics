
p = [0, 1, 0, 0, 0] # input distribution
world = ['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    '''
    This function returns
    '''

    q = []
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-pHit) * pMiss))
    sumQ = sum(q)

    for val in range(len(q)):
        q[val] = q[val]/sumQ

    return q

def move(p, U):
    '''
    Returns a new distribution 
    q, shifted to the right by U units. If U=0, q should 
    be the same as p.
    '''
    q = []
    for i in range(len(p)):
        q.append(p[(i-U) % len(p)])
    return q

# for entry in measurements:
#     p = sense(p, entry)

print(move(p, 0))
