from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

math_operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply
}
continue_calc = True

print(logo)
while continue_calc:
    acc = float(input("What's the first number?: "))

    while acc:
        operation = input('Pick an operation +, -, * or /: ')
        if operation not in math_operations.keys():
            print("Wrong operation type")
        else:
            arg = float(input("What's the second number?: "))
            result = math_operations[operation](acc, arg)
            print(f"{acc} {operation} {arg} = {result}")

            save_result = input(f'Type "y" to continue calculating with {result}, '
                                f'or type "n" to start a new calculation: ')
            if save_result == 'y':
                acc = result
            else:
                acc = 0