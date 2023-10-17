words = {}
hvl = float("-inf")

while True:
    prb = input()
    if prb == "$":
        break

    a, b = prb.split()

    if a not in words:
        words[a] = int(b)
    else:
        words[a] += int(b)

mvl = max(words.values())

max_key = [k for k, v in words.items() if v == mvl]
max_key.sort()
for i in max_key:
    print(i)