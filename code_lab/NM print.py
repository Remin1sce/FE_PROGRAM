n = int(input())
m = int(input())
count = 0

if n > 0 and m > 0:
    for i in range(n//m + 1):
        for j in range(m):
            if count < n:
                print(count, end=' ')
                count += 1
            else:
                break
        print()
else:
    print("Invalid input")                