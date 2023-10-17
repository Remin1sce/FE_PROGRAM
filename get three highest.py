a = []
while True:
  b = input()
  if b == "$":
    break
  else:
      a.append(int(b))
a=set(a)
a=list(a)      
if len(a) == 0:
  print("Insufficient data")
elif len(a)== 1:
   highest = sorted(a, reverse=True)

   highest_three = highest[0]
   print(highest_three)
elif len(a)== 2:
   highest = sorted(a, reverse=True)

   highest_three = highest[0]
   highest_two = highest[1]
   print(highest_three)
   print(highest_two)
else:
   highest = sorted(a, reverse=True)


   highest_three = highest[0]
   highest_two = highest[1]
   highest_one = highest[2]
   print(highest_three)
   print(highest_two)
   print(highest_one)
   


