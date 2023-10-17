xa1 = int(input())
ya1 = int(input())
xa2 = int(input())
ya2 = int(input())
xb1 = int(input())
yb1 = int(input())
xb2 = int(input())
yb2 = int(input())

if xa2 > xb1 and yb1 > ya2:
    print((xa2-xb1)*(yb1-ya2))
else:
    print('0')