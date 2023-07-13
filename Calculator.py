import sys


def start():
    print('\nWelcome to the BasicCalculator!\nPlease Select An Option Given Below.\n')
    selected_options = options()
    perform_calculation(selected_options)


def options():
    options = ['#1 Enter + to add', '#2 Enter - to subtract',
               '#3 Enter x to multiply', '#4 Enter / to divide']

    for i in range(0, len(options)):
        print(options[i])

    user_input = validate_input(input("> "))

    x = input('Enter the value of x: ')
    y = input('Enter the value of y: ')

    results = [user_input, int(x), int(y)]
    return results


def validate_input(usr_input):
    # Validate user input and allow user to reselect the options if it's not a valid operation
    if usr_input not in ('+', '-', 'x', '/'):
        print('\nInvalid Input! Please Select An Option Given Below.\n')
        options()
    else:
        return usr_input


def perform_calculation(selected_options):
    # Perform the selected calculation based on user input
    selected_operation = selected_options[0]
    x = selected_options[1]
    y = selected_options[2]

    # Use match-case to handle different operations
    match selected_operation:
        case '+':
            add(x, y)
        case '-':
            subtract(x, y)
        case 'x':
            multiply(x, y)
        case '/':
            divide(x, y)
        case _:
            print('...')
            sys.exit()

    reload_input = input('Would you like to reload? (y/n): ').lower()
    reload(reload_input)


def reload(reload_input):
    # Reload or terminate based on user input
    match reload_input:
        case 'y':
            start()
        case 'n':
            print('Thank you for using BasicCalculator! Terminating...')
            sys.exit()
        case _:
            print('Invalid Input! Terminating...')
            sys.exit()


def add(x, y):
    # Add two numbers
    result = x + y
    print('Result: ', result)

    return result


def subtract(x, y):
    # Subtract two numbers
    result = x - y
    print('Result: ', result)

    return result


def multiply(x, y):
    # Multiply two numbers
    result = x * y
    print('Result: ', result)

    return result


def divide(x, y):
    # Divide two numbers
    result = x / y
    print('Result: ', result)

    return result


start()
