amount = int(input())

min_x = float('inf')
max_x = -float('inf')
min_y = float('inf')
max_y = -float('inf')

for i in range(amount):
    input1 = input()
    splitted = input1.split()
    x = int(splitted[0])
    y = int(splitted[1])

    if x < min_x:
        min_x = x
    if x > max_x:
        max_x =x 
    if y < min_y:
        min_y = y
    if y > max_y:
        max_y = y

width = max_x - min_x
height = max_y - min_y
longest = max(width, height)
area = longest ** 2
print(area)