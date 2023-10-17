n = int(input())
m = int(input())

if n > 0 and m > 0:
    for j in range(1, m + 1):
        num = j
        while num <= n:
            print(num, end=" ")
            num += m
        print()
else:
    print("Invalid input") 
