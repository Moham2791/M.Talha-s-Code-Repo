def rotate():

    k = 2
    l = [1, 2, 3, 4, 5, 6]

    for i in range(k):
        c = l.pop()
        l.insert(0, c)
    print(l)


rotate()
