a = float(input())
b = float(input())
c = round(a/(b/100)**2, 2)
if c < 18.5:
    print(c)
    print("Below normal weight")
else:
    if c<25:
        print(c)
        print("Normal weight")
    else:
        if c<30:
            print(c)
            print("Overweight")
        else:
            if c<35:
                print(c)
                print("Class I Obesity")
            else:
                if c<40:
                    print(c)
                    print("Class II Obesity")
                else:
                    if c>=40:
                        print(c)
                        print("Class III Obesity")

                
