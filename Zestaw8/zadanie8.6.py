value = {(0,0) : 0.5, (1, 0) : 0.0, (0,1) : 1.0}

def P(i,j):
    if (i,j) in value.keys():
        return value[i,j]
    if j==0 and i>0:
        return 0.0
    if i==0 and j>0:
        return 1.0
    else:
        for n in range (1, i+1):
            for m in range (1, j+1):
                value[n,m] = 0.5 * (P(n-1,m) + P(n,m-1))
        return value[n,m]
    return value[n,m]

def P_rec(i,j):
    if (i,j) in value.keys():
        return value[i,j]
    if j==0 and i>0:
        return 0.0
    if i==0 and j>0:
        return 1.0
    else:
        return 0.5 * (P_rec(i-1,j) + P_rec(i,j-1))



print(P(5,4))
print(P_rec(5,4))