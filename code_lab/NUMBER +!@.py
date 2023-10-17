n = int(input())
m = int(input())
if n>0 and m>0:
    for i in range(m):
        for j in range(1, n+1):
            print(j + m)
else:
    print("Invalid Input")
