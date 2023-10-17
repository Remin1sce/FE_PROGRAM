yeahboi = None
combo = 0
max_combo = 0

while True:
    number = input()
        
    if number == '$':
        break
    else:
        number = int(number)
        if yeahboi == number:
            combo += 1
        else:
            combo = 1
        yeahboi = number
        
    if combo > max_combo:
            max_combo = combo


print(max_combo)