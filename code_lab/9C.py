def polymul(p1, p2):
    m, n = len(p1), len(p2)
    mulRes = [0] * (m + n - 1)

    for i in range(m):
        for j in range(n):
            mulRes[i + j] += p1[i] * p2[j]

    return mulRes

p = input()
pp = input()

p1 = list(map(int, p.split()))
p2 = list(map(int, pp.split()))

mulRes = polymul(p1, p2)

output = " ".join(map(str, mulRes))
print(output)