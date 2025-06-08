# Variables and Data Types

#trial 1
# name = input("Name: ")
# age = input("Age: ")
#
#
# century1 = 100 - int(age)
# century2 = int(century1) + 2025
#
# print(f"Name is: {name} \nAge is: {age} \nYear you will turn 100 (Current year 2025): {century2}")


#trial 2

# def century_calculator():
#     while True:
#         print("===== Century Calculator =====")
#         name = input("Name: ")
#         age = input("Age: ")
#
#         century1 = 100 - int(age)
#         century2 = int(century1) + 2025
#
#         print(f"Name is: {name} \nAge is: {age} \nYear you will turn 100 (Current year 2025): {century2}")
#         print()
#
#
# # call
# century_calculator()


# trial 3 IMPROVED
# - with validation
# - with Error handling


def century_calculator():
    while True:
        print("======== Century Calculator ========")

        # validate
        name = input("Enter name (or type 'exit' to quit): ")
        if name.lower() == 'exit':
            print("Goodbye!")
            break

        try:
            age = int(input("Enter age: "))
            if age < 0:
                print("Invalid input. Please enter a valid number.")
                print()
                continue

        except ValueError:
            print("Invalid input. Please enter a valid number.")
            print()
            continue

        # calculate
        century_year = (100 - age) + 2025

        # print
        print(f"Name: {name}\nAge:{age}\nYear you will turn 100: {century_year}")
        print()


century_calculator()