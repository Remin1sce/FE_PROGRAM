n = int(input())
current_person = 1
print(current_person)

for i in range(n):
    current_person = (current_person+3) % n
    if current_person == 0:
        current_person = n
    if current_person == 1:
        break
    print(current_person)