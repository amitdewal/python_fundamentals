try:
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    result = num1 / num2
    print("the result is:",result)

except ZeroDivisionError as e:
    print("You can't divide by zero. please enter a non-zero number",e)

except Exception as e:
    print("Something went wrong, please enter valid numeric values",e)
