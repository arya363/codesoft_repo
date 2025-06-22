def calculator():
    print("📟 Simple Calculator")
    
    # Get user input
    try:
        num1 = float(input("Enter the first number: "))
        op = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("❌ Invalid input. Please enter numbers only.")
        return

    # Perform operation
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            print("❌ Cannot divide by zero.")
            return
        result = num1 / num2
    else:
        print("❌ Invalid operation.")
        return

    # Display result
    print(f"✅ Result: {num1} {op} {num2} = {result}")

# Run the calculator
calculator()
