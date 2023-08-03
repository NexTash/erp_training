def sum(x, y):
    return x + y

def product(x, y):
    return x * y

def diffrence(x, y):
    return x - y

def division(x, y):
    return x / y

choice = "y"
while choice == "y":
    x = int(input("First Value: "))
    y = int(input("Second Value: "))
    operator = input("Give Operation, e.g +, -, *, / :")
    
    if operator == "+":
        _sum = sum(x, y)
        print("Sum =", _sum)

    elif operator == "-":
        _diffrence = diffrence(x, y)
        print("Diff =", _diffrence)

    elif operator == "*":
        _product = product(x, y)
        print("Product =", _product)

    elif operator == "/":
        _division = division(x, y)
        print("Divison =", _division)
        
    else:
        print("invalid operation")


    choice = input("\n\nIf want to recalculate press y else any other key to terminate: ")
