n= int(input())
for i in range(1, n):
        for j in range(i+1, n):
            for k in range(j+1, n+1):
                print(f"({i},{j},{k})")