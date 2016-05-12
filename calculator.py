import sys    #for the exit()

while True:  #i found this try: for debugging, but it works fine here
    try:
        number_1 = float(input('Enter first number(or letter to EXIT): '))
    except ValueError:
        exit()
    else:
        break

operation = input("Enter an operation:")
number_2 = float(input('Enter second number: '))    #float() for the floating point numbers


if operation == "+":
    sum = float(number_1) + float(number_2)
elif operation == "-":
    sum = float(number_1) - float(number_2)
elif operation == "*":
    sum = float(number_1) * float(number_2)
elif operation == "/":
    sum = float(number_1) / float(number_2)
else:
    exit()

print('The result is {0}'.format(sum)) #print the result on screen
