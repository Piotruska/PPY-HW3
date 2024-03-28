# Task 1
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
    acceptable_chars = chars.split()

    if len(remove_chars_array) != 0:
        for char in remove_chars_array:
            if char in acceptable_chars:
                acceptable_chars.remove(char)

    password = ''.join(random.choice(acceptable_chars) for x in range(length))
    return password



