a = []
while True:
  b = input()
  if b == "$":
    break
  else:
      a.append(int(b))
if len(a) == 0:
  print("Invalid input")
else:
 print(min(a))
 print(max(a))




    