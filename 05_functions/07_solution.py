# 7. Function with *args
# Problem: Write a function that takes variable number of arguments and returns their sum.

# def sumAll(*args):
#     return sum(args)

# print(sumAll(1, 2, 3))
# print(sumAll(1, 2, 3, 4))
# print(sumAll(1, 2, 3, 4, 5))

def sumAll(*args):
    print(args)
    for i in args:
        print(i * 2)
    return sum(args)

print(sumAll(1, 2, 3))