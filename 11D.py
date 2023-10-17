sum = 0
min = 0

while True:
    value = input()
    if value == "$":
        break

    value = int(value)
    sum = sum + value
    if sum < min:
        min = sum

print(abs(min))