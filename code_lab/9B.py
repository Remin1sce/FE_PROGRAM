a = str(input())
b = a.split()
b2 = [float(i) for i in b]

c = str(input())
d = c.split()
d2 = [float(i) for i in d]

x = 0
for me in range(0, len(d2)):
    x += d2[me]*b2[me]
print(x)