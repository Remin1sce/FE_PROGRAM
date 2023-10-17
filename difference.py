b =[]
d = []
while True:
    a = input()
    if a != '$':
        b.append(a)
    else:
        break
for i in range(1, len(b)):
    subtract = abs(int(b[i]) - int(b[i-1]))
    d.append(subtract)
if len(b) <= 1:
    print("Insufficient data")
else:
    print(max(d))