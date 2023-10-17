a = int(input())
if 0<a<=20:
    for i in range(a,0, -1):
            print((a-i)*' '+i*'*')
else:
    print("Invalid input")            

        