x = abs(int(input()))
list_of_digits = [int(i) for i in str(x)]
print(sum(set(list_of_digits)))
