thb = float(input())
currency = str(input())
if currency == "USD":
    print(int(thb/34.20))
    print(round(thb%34.20,2))
elif currency == "EUR":
    print(int(thb/38.47))
    print(round(thb%38.47,2))
elif currency == "GBP":
    print(int(thb/44.73))
    print(round(thb%44.73,2))
elif currency == "JPY":
    print(int(thb/0.2476))
    print(round(thb%0.2476,2))
        

        