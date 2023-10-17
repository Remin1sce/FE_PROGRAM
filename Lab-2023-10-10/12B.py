x = input()
try:
    file = open(x, 'r')
    for line in file:
        print(line, end = '')
    file.close()
except Exception:
    print("ERROR: File not found")