def fun(i):
    if i>0:
        print("A"*i)
        fun(i-1)
        print("B"*i)
fun(5)