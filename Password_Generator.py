import string 
import random

Uletters=string.ascii_uppercase
Lletters=string.ascii_lowercase
numbers=string.digits
punctuation=string.punctuation

def shuffle(string):
    tempList=list(string)
    random.shuffle(tempList)
    return ''.join(tempList)
uppercaseLetter1=random.choice(Uletters)
uppercaseLetter2=random.choice(Uletters)
lowercaseLetter1=random.choice(Lletters)
lowercaseLetter2=random.choice(Lletters)
digit1=random.choice(numbers)
digit2=random.choice(numbers)
punctuationSign1=random.choice(punctuation)
punctuationSign2=random.choice(punctuation)

password=uppercaseLetter1+uppercaseLetter2+lowercaseLetter1+lowercaseLetter2+digit1+digit2+punctuationSign1+punctuationSign2
print(shuffle(password))
