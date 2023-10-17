x = int(input())
y = int(input())
z = int(input())
hours = 0
days = 0
y = y + z
hours = y//60
y = y%60
x = x + hours
days = x//24
x = x%24

if 0<=y<=9:
    y = "0" + str(y)
else:
    y = str(y)
if 0<=x<=9:
    x = str("0" + str(x))
else:
    x = str(x)
if days == 0:
    print(x + ":" + y)
elif abs(days) == 1:
     if days>0:
         print(x + ":" + y + " + " + str(days) + " day")
     else:
          print(x + ":" + y + " - " + str(-days) + " day")
else:
        if days>0:
         print(x + ":" + y + " + " + str(days) + " days")
        else:
         print(x + ":" + y + " - " + str(-days) + " days")

