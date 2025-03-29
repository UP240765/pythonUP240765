import random as rd
import string

#Writ a function which generates a six digit/character random_user_id
def random_user_id():
    word = ''
    char = string.ascii_letters + string.digits
    for i in range(6):
        x = rd.randint(0,len(char))
        word += char[x]
    return word
        

#Modify the previous task. Declare a function named user_id_gen_by_user.
def user_id_gen_by_user():
    word = ''
    numChar = int(input("Enter the number of characters: "))
    numUser = int(input("Enter the number of user names: "))
    char = string.ascii_letters + string.digits
    for c in range(numUser):
        for i in range(numChar):
            x = rd.randint(0,len(char))
            word += char[x]
        print(word)
        word = ''

#Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    r = rd.randint(0,255)
    g = rd.randint(0,255)
    b = rd.randint(0,255)
    rgb =  [r,g,b]
    return rgb

print(rgb_color_gen())
