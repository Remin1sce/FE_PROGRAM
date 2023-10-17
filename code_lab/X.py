n = int(input())
if n in range(1, 30) and n % 2 == 1:
    for i in range(0, n//2):
        print(' '*i + '\\' + ' '*(n-2*(i+1)) + '/')
    print(' '*(n//2) + 'X')
    for j in range(n//2, 0, -1):
        print(' '*(j-1) + '/' + ' '*(n-2*j) + '\\')
else:
    print('Invalid input')
