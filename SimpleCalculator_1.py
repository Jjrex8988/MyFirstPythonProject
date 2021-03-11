def add(x, y):
    """Add two numbers"""
    return x + y


def subtract(x, y):
    """Subtracts two numbers"""
    return x - y


def multiply(x, y):
    """Multiples two numbers"""
    return x * y


def divide(x, y):
    """Divides two numbers"""
    return x / y


def modulus(x, y):
    """Divide two numbers, take the remainder"""
    return x % y


def power(x, y):
    """Power two numbers"""
    return x ** y


def division(x, y):
    """Integer division (ignore any remainder)"""
    return x // y


# Define function to obtain which function the user wants

def get_operation_choice():
    input_ok = False
    while not input_ok:
        print('Menu Options are: ')
        print('\t1. Add')
        print('\t2. Subtract')
        print('\t3. Multiply')
        print('\t4. Divide')
        print('\t5. Modulus')
        print('\t6. Power')
        print('\t7. Integer Division')
        print('-' * 38)
        user_selection = input('Please make a selection: ')
        if user_selection in ('1', '2', '3', '4', '5', '6', '7'):
            input_ok = True
        else:
            print('Invalid Input (Must be 1 - 7)')
    print('-' * 38)
    return user_selection


def get_numbers_from_user():
    """ Obtain two number from the user"""

    num1 = get_integer_input('Input the first number: ')
    num2 = get_integer_input('Input the Second number: ')
    return num1, num2


def get_integer_input(message):
    """Obtain input from user and convert to an int"""

    value_as_string = input(message)
    while not value_as_string.isdecimal() and value_as_string.isnumeric():
        print('The Input must be an integer')
        value_as_string = input(message)

    return float(value_as_string)

def check_if_user_has_finished():
    """
     Check that the users wants to finish or not.
     Performs some verification of the input."""

    ok_to_finish = True
    user_input_accepted = False

    while not user_input_accepted:
        user_input = input('Do you want to finish (y/n): ')
        if user_input == 'y':
            user_input_accepted = True
        elif user_input == 'n':
            ok_to_finish = False
            user_input_accepted = True
        else:
            print('Response must be (y/n), please try again')
    return ok_to_finish


print('Simple Calculator App')

finished = False
while not finished:
    result = 0

    menu_choice = get_operation_choice()

    n1, n2 = get_numbers_from_user()

    # Get the operation from the user
    # Get the number from the user
    # Select the operation

    if menu_choice == '1':
        result = add(n1, n2)
    elif menu_choice == '2':
        result = subtract(n1, n2)
    elif menu_choice == '3':
        result = multiply(n1, n2)
    elif menu_choice == '4':
        result = divide(n1, n2)
    elif menu_choice == '5':
        result = modulus(n1, n2)
    elif menu_choice == '6':
        result = power(n1, n2)
    elif menu_choice == '7':
        result = division(n1, n2)

    print('Result: ', result)
    print('=' * 38)
    finished = check_if_user_has_finished()

print('Bye')
