n = int(input())
fav = []

for i in range(n):
    food = (input())
    fav.append(food.split())

fav_set = [set(sublist) for sublist in fav]
intersection = fav_set[0].intersection(*fav_set[1:])
intersection_list = " ".join(sorted(intersection))
if intersection_list == "":
    print("Nothing")
else:
    print(intersection_list)