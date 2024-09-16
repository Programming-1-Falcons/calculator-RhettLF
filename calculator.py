#☭
#Peter Griffin
while True:

    print("Welcome to Lynwood technology!")
    print("-----------------------------")
    num1 = float(input("Please enter the first number you want to use. \n"))
    operation = input("Please enter a mathmatical opperation: \n")
    if operation != "+" and operation != "-" and operation != "/" and operation != "*" and operation != "^":
        print("I am sorry, Lynwood technology is still in development. Try using '+, -, /, *, or ^' instead!")
        continue
    num2 = float(input("Please enter the second number you want to use. \n"))

    if operation == "+":
        result = (num1 + num2)
        print(num1, operation, num2, "=", float(result))
    elif operation == "-":
        result = (num1 - num2)
        print(num1, operation, num2, "=", float(result))
    elif operation == "/":
        result = (num1 // num2)
        print(num1, operation, num2, "=", float(result))
    elif operation == "*":
        result = (num1 * num2)
        print(num1, operation, num2, "=", float(result))
    elif operation == "^":
        result = (num1 ** num2)
        print(num1, operation, num2, "=", float(result))