a = int(input())
b = int(input())
c = int(input())
if a<=b<=c or c<=b<=a:
    print(b)
else:
    if b<=a<=c or c<=a<=b:
      print(a)
    else:
        if b<=c<=a or a<=c<=b:
           print(c)
    