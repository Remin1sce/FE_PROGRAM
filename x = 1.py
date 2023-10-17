a = []
while True:
  b = input()
  if b == "$":
    break
  else:
      a.append(int(b))
def print_minimum_ignore_negative(numbers):
    positive_numbers = [num for num in numbers if num >= 0]
    if not positive_numbers:
        print("None")
    else:
        min_value = min(positive_numbers)
        print(min_value)
print_minimum_ignore_negative(a)


