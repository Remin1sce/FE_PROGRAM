def min(x,y,z):
    if z<= y and z<= x:
        return z
    elif y <= z and y<=x:
        return y
    elif x<=z and x<=y:
        return x

a = int(input())
b = int(input())
c = int(input())
print(min(a,b,c))