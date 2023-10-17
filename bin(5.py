x = float(input())
s = ''
a = int(x)
binary = ''
b = float(x) - int(x)
if 0<=a<=2**20:
    while a> 0:
     z = a%2
     a = a//2
     s = str(z) + s
    if s == '':
        s = '0'
 
    for _ in range(30):
            b *= 2
            if b>=1:
             b-=1
             binary_digit = 1
             binary += str(binary_digit)
            else:
                binary_digit = 0
                binary += str(binary_digit)

            
    print(s + '.' + binary)
else:
    print("Invalid input")
     




