import turtle as t

f = open('picture.txt', 'r')
t.Turtle()
while True:
    lines = f.readline()
    print(lines)
    if lines == '\n':
        t.penup()
        continue
    else:
        l = lines.split(',')
        if l[0] != '':
            x = float(l[0])
            y = float(l[1])
            t.goto(x,y)
            t.pendown()
        else: break
