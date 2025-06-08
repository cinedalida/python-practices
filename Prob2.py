# control flow

def even_odd():
    num = int(input("Enter Number: "))
    if num <= 0:
        print("Invalid input. Please enter a positive number.")
        return

    if num % 2 == 0:
        print(f"Number: {num} is even")
        for i in range(2, num+1, 2):
            print(i)

    else:
        print(f"Number: {num} is odd")
        for i in range(1, num+1, 2):
            print(i)


even_odd()