xa1 = int(input())
ya1 = int(input())
xa2 = int(input())
ya2 = int(input())
xb1 = int(input())
yb1 = int(input())
xb2 = int(input())
yb2 = int(input())

if(yb2 > ya1 or ya2 > yb1) or (xa2 < xb1 or xb2 < xa1) :
    print(0)
else:
    x = min(xa2,xb2) - max(xa1,xb1)
    y = min(ya1,yb1) - max(ya2,yb2)
    print(x*y)