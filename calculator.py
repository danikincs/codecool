num1 = int(input('Enter first number(or letter to EXIT): '))
operation = input("Enter an operation:")
num2 = int(input('Enter second number: '))


if operation == "+":
    sum = float(num1) + float(num2)
elif operation == "-":
    sum = float(num1) - float(num2)
elif operation == "*":
    sum = float(num1) * float(num2)
elif operation == "/":
    sum = float(num1) / float(num2)

# Display the the result
print("The Result is:{0}".format(sum))
