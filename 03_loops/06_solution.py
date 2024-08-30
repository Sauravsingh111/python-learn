# 6. Factorial Calculator
# Problem: Compute the factorial of a number using a while loop.

num = 4
fact = 1

while num > 0:
    fact = fact * num
    num = num - 1

print(fact)