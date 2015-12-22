def reader(f):
    D = {}
    for x in f:
        for c in x:
            if c in D:
                D[c] += 1
            else:
                D[c] = 1
    return D

fp = open('test1.txt')
A = reader(fp)
print(A['t'])   # Line 1
print(len(A))   # Line 2
print(D['e'])   # Line 3
