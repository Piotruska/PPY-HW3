#Task 1
import random
import string


def generate_password(add_digits=True,
                      add_letters=True,
                      add_special=True,
                      remove_characters="",
                      length=8):
    chars = ''
    if add_digits:
        chars += string.digits
    if add_letters:
        chars += string.ascii_letters
    if add_special:
        chars += string.punctuation

    remove_chars_array = remove_characters.split()
    acceptable_chars = list(chars)

    for char in remove_chars_array:
        if char in acceptable_chars:
            acceptable_chars.remove(char)

    password = ''.join(random.choice(acceptable_chars) for _ in range(length))
    return password

def get_yn_input(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response == 'y' or response == 'n':
            return response
        print("Invalid input. Please enter 'y' or 'n'.")

def get_int_input(prompt):
    while True:
        response = input(prompt).strip()
        if response.isdigit():
            return int(response)
        print("Invalid input. Please enter a number.")

def password_generator_program():
    run_program = True
    while run_program:
        add_digits = get_yn_input("Include digits? (y/n): ").lower() == 'y'
        add_letters = get_yn_input("Include letters? (y/n): ").lower() == 'y'
        add_special = get_yn_input("Include special characters? (y/n): ").lower() == 'y'
        remove_characters = input("Enter characters to remove: ")
        length = get_int_input("Password length: ")

        if length < 8:
            print("Password length cannot be smaller than 8 characters.")
            continue

        password = generate_password(add_digits, add_letters, add_special, remove_characters, length)
        print("Generated password:", password)

        confirm = input("Confirm password? (y/n): ").lower()
        if confirm == 'y':
            run_program = False

password_generator_program()


# Task 2

def order_pizza():
    run_program = True
    while run_program:
        print("Welcome to the Pizza Ordering System!")
        toppings = input("Enter toppings separated by commas: ").split(',')
        size = input("Enter size (small, medium, large): ").lower()
        crust_type = input("Enter crust type (thin, thick): ").lower()
        make_pizza(*toppings, size=size, crust=crust_type)

        choice = input("Do you want to order another pizza? (yes/no): ").lower()
        if choice != 'yes':
            print("Thank you for using the Pizza Ordering System. Have a great day!")
            run_program = False


def make_pizza(*toppings, **kwargs):
    size = kwargs.get('size')
    crust = kwargs.get('crust')
    price = 0
    toppings_number = len(toppings)

    if toppings_number < 2 or toppings_number > 7:
        print("Error: Invalid number of toppings.")
        return
    else:
        price = calculate_price(size, crust, toppings_number)
        print("--------------------------")
        print("Ordered Pizza:")
        print("--------------------------")
        print("Size:", size)
        print("Crust Type:", crust)
        print("Toppings:", ', '.join(toppings))
        print("Total Price: $", price)
        print()


def calculate_price(size, crust, toppings_number):
    total_price = 0
    size_price = {'small': 10, 'medium': 15, 'large': 20}
    crust_prices = {'thin': 0, 'thick': 3}
    total_price += size_price[size] + crust_prices[crust]
    if toppings_number > 2:
        for _ in range(toppings_number - 2):
            total_price += 2
    return total_price

order_pizza()