def count_down(a):
    if a == 0:
        print(a)
        return
    else:
        print( a)
        count_down(a - 1)

a = 6
count_down(a)