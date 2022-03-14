import random
import string

while True:
    try:
        char_num = int(input("Podaj liczbe znakow. Minimum 8:  "))
        if char_num < 8:
            print('Za malo znakow. Wybierz ponownie!')
        else:
            break
    except:
        print('Podaj liczbe znakow!')

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

all_characters = lower + upper + digits + symbols
random_characters = random.sample(all_characters, char_num)

password = ''.join(random_characters)

print(password)

