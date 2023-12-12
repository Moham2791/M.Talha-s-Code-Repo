l1 = ['a', 'b']
l2 = [1, 2, 3]

print(l1+l2)


def concat(l1, l2):
    print("What is the first list of numbers ?")
    l1 = list(input())
    print("What is the second list of numbers ?")
    l2 = list(input())
    print(l1+l2)


concat(l1, l2)
