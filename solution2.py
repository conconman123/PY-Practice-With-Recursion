def count_up(a, b):
    
    if a > b:
        return
    else:
        print(a)
        a += 1
        count_up(a , b)

b = 10

count_up(1, b)