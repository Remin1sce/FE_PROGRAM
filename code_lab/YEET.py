def remove_negatives(x):
    for i in range(len(x)-1, -1, -1):
        if x[i]<0:
            del x[i]
q = [10,-2,0,-3,-2,5,0]
remove_negatives(q)
print(q)

