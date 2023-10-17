maxw = minw = None
while True:
    x = input()
    if  x != '$' and maxw == None:
        maxw = minw = int(len(x))
    elif x == '$':
        break
        if int(len(x))< minw:
            minw= x
        elif int(len(x))> maxw:
            maxw = x
print(maxw)
print(minw)
        
            
    
            
