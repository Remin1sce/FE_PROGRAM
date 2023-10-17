sum_so_far = 0
while True:
  n = input()
  if n == '$':
    print(sum_so_far)
    break
  sum_so_far += int(n)