def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
        print("just something")

    return a / b


def calculator():
    print("Simple Calculator")
    print("Available operations: +, -, *, /")

    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter the operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    if operator == "+":
        result = add(num1, num2)
    elif operator == "-":
        result = subtract(num1, num2)
    elif operator == "*":
        result = multiply(num1, num2)
    elif operator == "/":
        try:
            result = divide(num1, num2)
        except ZeroDivisionError as e:
            print(e)
            return
    else:
        print("Invalid operator. Please use +, -, *, or /.")
        return

    print(f"Result: {num1} {operator} {num2} = {result}")


if __name__ == "__main__":
    calculator()
