retry = " "
while retry != "no":
    letter = input("enter P to do power or O to do other operations: ")

    if letter == "O":
        num1 = float(input("enter the first number: "))
        operator = input("enter the operator: ")
        num2 = float(input("enter the second number: "))

        if operator == "+":
            print(num1 + num2)
        elif operator == "-":
            print(num1 - num2)
        elif operator == "*":
            print(num1 * num2)
        elif operator == "/":
            print(num1 / num2)
        else:
            print("wrong operator please try again")
        retry = input("do you want to try again? yes or no: ")

    elif letter == "P":
        num1 = float(input("enter the first number: "))
        num2 = float(input("enter the second number: "))
        def power (num1, num2):
            return num1 ** num2
        print(power(num1, num2))
        retry = input("do you want to try again? yes or no: ")
