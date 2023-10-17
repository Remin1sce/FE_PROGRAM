line1 = str(input())
line1 += " "
line1 += line1
line2 = str(input())
tup2 = tuple(line2.split(' '))
revtup2 = tup2[::-1]
revline2 = ""
for x in revtup2:
  revline2 += x
  revline2 += " "
same = line2 in line1
revsame = revline2 in line1
if not same and not revsame:
  print("different")
else:
  print("same")