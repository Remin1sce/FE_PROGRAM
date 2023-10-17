ones = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
        5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
tens = {10: 'ten', 11: 'eleven', 12:  'twelve', 13: 'thirteen', 14: 'fourteen',
        15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
        20:  'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
        60: 'sixty', 70: 'seven', 80: 'eighty', 90: 'ninety'}

input = int(input())
if input in range(1000):
    if input <= 9:
        print(ones[input])
    elif 10 <= input <= 20:
        print(tens[input])
    elif 21 <= input <= 99:
        a = input // 10 * 10 #Tens หลักสิบ // -> no remainder
        b = input % 10 #Ones หลักหน่วย
        out = tens[a]
        if b > 0:
            out = out + " " + ones[b]
        print(out)
    else:
        a = input // 100 
        b = (input % 100) // 10 * 10
        c = input % 10
        out = ones[a] + " hundred"
        if b > 0 and c > 0:
            if b == 10:
                out = out + " and " + tens[b + c]
            else:
                out = out + " and " + tens[b] + " " + ones[c]
        elif b > 0:
            out = out + " and " + tens[b]
        elif c > 0:
            out = out + " and " + ones[c]
        print(out)