from bs4 import BeautifulSoup
def password_selector():
    confirmed = False
    while confirmed == False:
        print('Select "A" for password generator or "B" for password validator')
        choice = input('Your Choice: ')
        print('Selected: ' +choice)
        if choice == 'a' or choice == 'A':
            confirmed = True
            password_generator()
        if choice == 'b' or choice == 'B':

def password_generator():
    print('password generator selected') 

def password_validator():
    print('password validator selected')     

password_selector()


class password:
    lowercase_letters: [str]
    uppercase_letters: [str]
    numbers: [str]
    special_characters: [str]