import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    pool = ""
    if use_letters:
        pool += string.ascii_letters
    if use_numbers:
        pool += string.digits
    if use_symbols:
        pool += string.punctuation

    if not pool:
        raise ValueError("Выберите хотя бы один тип символов!")

    return ''.join(random.choice(pool) for _ in range(length))

def validate_length(length_val):
    if not (4 <= length_val <= 64):
        return False, 
    return True, ""