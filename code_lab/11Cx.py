import math

num = int(input())
list1 = []
garbage = []


def average(x):
    avg = sum(x) / len(x)
    return avg


for i in range(num):
    salary = int(input())
    list1.append(salary)

list2 = list1.copy()

avg = average(list1)

for i in range(len(list1)):
    list1[i] = (list1[i] - avg) ** 2

sd = math.sqrt(sum(list1) / len(list1))
sd = round(sd, 2)

a = avg + sd
b = avg - sd

for i in range(len(list2)):
    if list2[i] < b or list2[i] > a:
        garbage.append(list2[i])

for i in garbage:
    list2.remove(i)

ans = average(list2)
print(round(ans, 2))