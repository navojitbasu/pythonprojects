import string
import random

def generator():
    s1 = string.ascii_uppercase
    #print(s1)
    s2 = string.ascii_lowercase
    #print(s2)
    s3 = string.digits
    #print(s3)
    s4 = string.punctuation
    #print(s4) 

    passlen = int(input("Enter the password length\n: "))

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)
    #print(s)
    pas = ("".join(s[0:passlen]))
    print(pas)


generator()