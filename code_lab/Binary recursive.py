x = int(input())
def binary(a):
    global s
    if a == 0:
        print(s)
    else:
        z = a%2
        a = a//2
        s = str(z) + s
        binary(a)
s=''
if x==0:
    print(0)
else:            
    binary(x)