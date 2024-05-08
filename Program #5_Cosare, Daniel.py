# Program by Daniel Rein M. Cosare
# Do the programming exercise on CMPE-103-Module-3-Exception-Handling-in-Python. Page21.
# Date Created: May 8, 2024

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y


def calculator():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            print("Choose operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            choice = input("Enter choice (1/2/3/4): ")

            if choice == '1':
                print("The Result is:", add(num1, num2))
            elif choice == '2':
                print("The Result is:", subtract(num1, num2))
            elif choice == '3':
                print("The Result is:", multiply(num1, num2))
            elif choice == '4':
                print("The Result is:", divide(num1, num2))
            else:
                print("Invalid choice")
                continue

        except ValueError as e:
            print("Invalid input:", e)

        try:
            again = input("Do you want to try again? (yes/no): ")
            if again.lower() != 'yes':
                print("Thank you!")
                break
        except KeyboardInterrupt:
            print("Thank you!")
            break


if __name__ == "__main__":
    calculator()
