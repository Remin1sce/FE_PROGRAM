n = int(input())
store = {}

def times(x):
    if x not in store:
        store[x] = 1
    else:
        num = store[x]
        num += 1
        del store[x]
        store[x] = num

for food in range(n):
    am = input()
    times(am)

          
for k,v in sorted(store.items(), key = lambda x:(x[1],x[0])):
    print(f"{k} {v}")
    