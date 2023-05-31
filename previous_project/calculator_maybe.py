import logo

print(logo.logo_calculator)


def multiply(a, b):
    return a * b


def add(a, b):
    return a + b


def divide(a, b):
    return a / b


def subtract(a, b):
    return a - b


operations = {
    "-": subtract,
    "+": add,
    "/": divide,
    "*": multiply,
}

def calculator():
    a = float(input("Enter the first number: "))

    restart = ""

    while restart != 'n':
        for operation in operations:
            print(operation)
        mark = input("Enter the operation you want to do: ")

        b = float(input("Enter the second number: "))

        answer = operations[mark](a,b)

        print(f"{a} {mark} {b} = {answer}")

        restart = input("Type 'y' if you want to continue or 'n' if you want to start over: ")

        if restart == 'y':
            a = answer
        else:
            calculator()

calculator()