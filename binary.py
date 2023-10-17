x = int(input())
y = 0
s = ""
if 0<x<=2**20:
    while x> 0:
     z = x%2
     x = x//2
     s = str(z) + s
elif x == 0:
   print(0)
else:
    print("Invalid input")
print(s)

