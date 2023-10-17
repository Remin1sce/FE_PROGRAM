# Provide your code for function avg here
def avg(num1, num2 = None, num3 = None):
    if num2 is None and num3 is None:
        return round(float(num1), 2)
    elif num3 is None:
        return round((num1 + num2) / 2, 2)
    else:
        return round((num1 + num2 + num3) / 3, 2)
    



a = int(input())
b = int(input())
c = int(input())
print(avg(a,b,c))
print(avg(a,b))
print(avg(a))