

print("Enter a number:")
x = int(input())

print("Enter a 2nd number:")
y = int(input())

while True:
    print("Enter an operation (+, -, *, /):")
    xy = input()

    if xy in ["+", "-", "*", "/"]:
        break
    else:
        print("Error: Invalid operation! Please try again.\n")

if xy == "*":
    print("Result:", x * y)
elif xy == "+":
    print("Result:", x + y)
elif xy == "-":
    print("Result:", x - y)
elif xy == "/":
    if y != 0:
        print("Result:", x / y)
    else:
        print("Couldn't divide by zero.")

