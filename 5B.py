def progress(x=1, y=10):
    for j in range(0, y):
            print(j*x)
    
    


input()
d = input()
n = input()
input()
if (d!='') and (n!=''):
    d = int(d)
    n = int(n)
    progress(d,n)
elif (d!=''):
    d = int(d)
    progress(d)
elif (n!=''):
    n = int(n)
    progress(y=n)
else:
    progress()