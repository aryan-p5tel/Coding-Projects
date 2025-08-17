#test calculator code, non graphical

num1 = int(input("Enter first number: "))

while True:
    operation = input("Enter operation: ")

    if operation == "STOP":
        print("Calculator stopped.")
        break

    if operation == "=":
        print("Result:", num1)
        continue

    if operation not in ["+", "-", "*", "/", "%"]:
        print("Invalid operation")
        continue

    num2 = int(input("Enter next number: "))

    if operation == "+":
        num1 = num1 + num2
    elif operation == "-":
        num1 = num1 - num2
    elif operation == "*":
        num1 = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("Error: Division by zero!")
            continue
        num1 = num1 / num2
    elif operation == "%":
        num1 = num1 % num2  # modulus calc, not percentage
