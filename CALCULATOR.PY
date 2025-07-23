def calculator():
    print("Simple Calculator")
    print("Operations: +  -  *  /")

    # Taking input from the user
    num1 = float(input("Enter first number: "))
    op = input("Enter operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    # Performing the operation
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print("Invalid operation")
        return

    # Displaying the result
    print(f"Result: {num1} {op} {num2} = {result}")

# Run the calculator
calculator()
