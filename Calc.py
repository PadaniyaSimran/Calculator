def add(a, b):
    c = a + b
    return c


def sub(a, b):
    c = a - b
    return c


def mul(a, b):
    c = a * b
    return c


def div(a, b):
    c = a / b
    return c


while True:
    operation = input(
        "Select Operation: \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Exit. \n")
    if operation in ["1", "2", "3", "4"]:
        x = float(input("Enter the number:\n"))
        y = float(input("Enter the number:\n"))
        if operation == '1':
            print(add(x, y))
        elif operation == '2':
            print(sub(x, y))
        elif operation == '3':
            print(mul(x, y))
        elif operation == '4':
            if int(y) == 0:
                print("Denominator cannot be a Zero.\n")
            else:
                print(div(x, y))
    elif operation == '5':
        break
    else:
        print("Invalid operation\n")
