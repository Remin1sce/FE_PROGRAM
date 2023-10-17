word = input()
key_count = 0
key = ''
result = ''
for i in word:
    if key == '':
        key = i
        key_count +=1
    elif i == key:
        key_count +=1
    elif i != key:
        if key_count == 1:
            print(key, end = '')
        else:
            print(str(key_count) + key, end = '')
        key_count = 1
        key = i
if key_count == 1:
    print(key, end = '')
else:
    print(str(key_count) + key, end = '')
    key_count = 1
    key = i
        

