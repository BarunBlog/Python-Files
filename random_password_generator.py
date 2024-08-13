import math
import random
import string

capital_letter = string.ascii_uppercase
small_letter = string.ascii_lowercase
digits = string.digits
symbols = '!@#$%^&*()'


def get_random_str(str, len):
    result_str = ''.join(random.choice(str) for i in range(len))
    return result_str

def password_generator(capital_letter_prob, small_letter_prob, digits_prob, symbols_prob, password_size):
    password = ""

    capital_letter_len = math.floor((capital_letter_prob/100) * password_size)
    small_letter_len = math.floor((small_letter_prob/100) * password_size)
    digits_len = math.floor((digits_prob/100) * password_size)
    symbols_len = math.floor((symbols_prob/100) * password_size)

    password = password + get_random_str(capital_letter, capital_letter_len)
    password = password + get_random_str(small_letter, small_letter_len)
    password = password + get_random_str(digits, digits_len)
    password = password + get_random_str(symbols, symbols_len)

    password = get_random_str(password, capital_letter_len+small_letter_len+digits_len+symbols_len)
    return password

def probability_for_each_set(password):
    capital_letter_len = 0
    small_letter_len = 0
    digits_len = 0
    symbols_len = 0
    passlen = len(password)

    for i in range(passlen):
        if password[i] in capital_letter:
            capital_letter_len = capital_letter_len + 1
        elif password[i] in small_letter:
            small_letter_len = small_letter_len + 1
        elif password[i] in digits:
            digits_len = digits_len + 1
        else:
            symbols_len = symbols_len + 1

    capital_letter_prob = math.floor((capital_letter_len/passlen) * 100)
    small_letter_prob = math.floor((small_letter_len/passlen) * 100)
    digits_prob = math.floor((digits_len/passlen) * 100)
    symbols_prob = math.floor((symbols_len/passlen) * 100)

    print(f"Probability for capital letter: {capital_letter_prob}%")
    print(f"Probability for small letter: {small_letter_prob}%")
    print(f"Probability for digits: {digits_prob}%")
    print(f"Probability for symbols: {symbols_prob}%")

password = password_generator(20, 40, 25, 15, 16)
probability_for_each_set(password)
print(password)
