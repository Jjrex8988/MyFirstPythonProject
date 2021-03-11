from art import logo4

def add(n, m):
    return n + m


def sub(n, m):
    return n - m


def mul(n, m):
    return n * m


def div(n, m):
    return n / m


ope1 = {"+": add, "-": sub, "*": mul, "/": div}


def calculator():
    print(logo4)

    n = float(input("What's the first number? "))

    for symbol in ope1:
        print(symbol)

    con = True

    while con:
        pick = input("Pick an operation: ")

        while pick not in ope1:
            print("Please choose the correct operation")
            pick = input("Pick an operation: ")

        m = float(input("What's the next number? "))

        calculation_function = ope1[pick]
        ans1 = calculation_function(n, m)

        print(f"{n} {pick} {m} = {ans1}")

        if input(f"Type 'y' to continue calculating with {ans1} or type 'n' to start a new calculation.: ").lower() == "y":
            n = ans1
        else:
            con = False
            calculator()

print(calculator())
