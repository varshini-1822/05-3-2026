def add(a, b):
    """
    Add two numbers and return the result.

    Parameters:
    a (float): First number
    b (float): Second number

    Returns:
    float: Sum of the two numbers
    """
    return a + b


def subtract(a, b):
    """
    Subtract the second number from the first number.

    Parameters:
    a (float): First number
    b (float): Second number

    Returns:
    float: Difference of the two numbers
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers.

    Parameters:
    a (float): First number
    b (float): Second number

    Returns:
    float: Product of the two numbers
    """
    return a * b


def divide(a, b):
    """
    Divide the first number by the second number.

    Parameters:
    a (float): First number
    b (float): Second number

    Returns:
    float: Division result if b is not zero
    None: If division by zero occurs
    """
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return a / b


def get_numbers():
    """
    Ask the user to enter two numbers and validate them.

    Returns:
    tuple: Two float numbers (num1, num2)
    Returns (None, None) if invalid input is entered.
    """
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("Error: Please enter valid numbers.")


def main():
    """
    Main function that runs the calculator program.
    It displays the menu, takes user input, and performs
    the selected arithmetic operation.
    """

    operations = {
        1: add,
        2: subtract,
        3: multiply,
        4: divide
    }

    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    try:
        choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Error: Choice must be a number.")
        return

    if choice not in operations:
        print("Invalid choice.")
        return

    num1, num2 = get_numbers()

    if num1 is None or num2 is None:
        return

    result = operations[choice](num1, num2)

    if result is not None:
        print("Result:", result)


# Start the program
main()