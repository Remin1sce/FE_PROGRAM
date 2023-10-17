import os
dc = open('dictionary.txt','r')
d = dc.readlines()
d = d[0].split()
i = input('Enter a file name: ')
c = 1
if os.path.isfile(i):
    f = open(i,'r')
    k = f.readlines()
    for j in k:
        w = j.split()
        for x in w:
            y = x.upper()
            if y in d:
                continue
            elif y =='/n':
                continue
            elif y[-1] == ',' or y[-1] == '.':
                y = [j for j in y ]
                y.pop(-1)
                y = ''.join(y)
                if y not in d:
                    print('Line ' + str(c) + ': '+ x)
            else:print('Line ' + str(c) + ': '+ x)
        c+=1
else:
    print('ERROR: Cannot open the file')