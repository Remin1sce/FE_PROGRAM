n = int(input())
k = int(input())

if n in range(10000000001) and k in range(1,11):
    for z in range(k):
        r = n%16
        n = n//16
        
    if r <= 9:
        print(r)
    elif r == 10:
        print("A")
    elif r == 11:
        print("B")
    elif r == 12:
        print("C")
    elif r == 13:
        print("D")
    elif r == 14:
        print("E")
    else:
        print("F")
else: print("Invalid input")