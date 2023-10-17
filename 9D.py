x = []
while True:
    num = input()
    if num != "$":
        x.append(num)
    elif num == "$":
        x.sort()
        if len(x)%2 == 0:
            mid_1 = int(x[len(x)//2-1])
            mid_2 = int(x[len(x)//2])
            median = float(mid_1+mid_2)/2
            print(round(median,1))
            break
        elif len(x)%2 != 0:
            median = float(x[(len(x)//2)])
            print(round(median,1))
            break