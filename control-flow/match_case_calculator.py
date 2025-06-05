# Prompt user for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

# Perform the calculation using match-case (Python 3.10+ required)
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result:.2f}.")
    case "-":
        result = num1 - num2
        print(f"The result is {result:.2f}.")
    case "*":
        result = num1 * num2
        print(f"The result is {result:.2f}.")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result:.2f}.")
    case _:
        print("Invalid operation selected.")