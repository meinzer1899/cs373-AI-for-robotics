#!/usr/bin/env python3
'''
This is text
'''

p = [0, 1, 0, 0, 0] # input distribution
world = ['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

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
        q[val] = q[val] / sumQ

    return q

def move(p, U):
    '''
    Returns a new distribution
    q, shifted to the right by U units. 
    Cyclic distribution (if extend last index, starts again at first index, e.g. for 0...4, 4+1 would be 0).
    If U=0, q should be the same as p.
    '''
    q = []
    for location in range(len(p)):

        val = pExact * p[(location-U) % len(p)]
        val += p[(location-U-1) % len(p)] * pOvershoot
        val += p[(location-U+1) % len(p)] * pUndershoot
        q.append(val)

    return q

# for entry in measurements:
#     p = sense(p, entry)

print(move(p, 1))
