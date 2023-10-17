import random
import string

from collections import defaultdit
def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage:
password = generate_random_password()
print(f"Random Password: {password}")
