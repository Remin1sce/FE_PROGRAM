x = abs(int(input()))
list_of_digits = [int(i) for i in str(x)]
a = sum(list(set(list_of_digits)))
print(a)