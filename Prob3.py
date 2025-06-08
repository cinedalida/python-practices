# Funcitons

# Recursion, Fibonacci


num = int(input("Enter number: "))

def fibo_recursion(num):

    #base case
    if num < 0:
        return 0

    elif num == 1:
        return 1

    else:
        return fibo_recursion(num-1) + fibo_recursion(num-2)

print(f"The fibonacci of this number: {num} is {fibo_recursion(num)}")


