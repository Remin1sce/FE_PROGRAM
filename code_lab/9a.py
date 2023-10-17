import math

x = 0
y = 0
z = []
while True:
    a = input()
    if a != "$":
        a = int(a)
        x += a
        z.append(a)
    elif a == "$":
        b = x/len(z)
        for me in range(0, len(z)):
            y += (z[me]-b)**2
        y = y/len(z)
        y = math.sqrt(y)
        y = round(y, 2)
        print(y)
        break