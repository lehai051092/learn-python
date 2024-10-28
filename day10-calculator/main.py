from art import logo


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calculations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        operation_symbol = input("Pick an operation +, -, *, /: ")
        num2 = float(input("What is the next number?: "))

        if operation_symbol not in calculations:
            print("Invalid input")
            return

        selected_calculation = calculations[operation_symbol]
        answer = selected_calculation(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if choice == "n":
            should_accumulate = False
            print("\n" * 20)
            calculator()
        elif choice == "y":
            num1 = answer
        else:
            print("Invalid input")
            return

calculator()

