x = int(input())
def powtwo(n):
    global c
    if n==0:
        return 
    else:
       str(print(' '*c+n*'*'))
       c+=1
       powtwo(n-1)
def num(p):
    global c,a
    if p==1:
        return
    else:
        c=a
        powtwo(p)
        a+=1
        num(p-1)

c=0
a=0       
        
        
num(x)