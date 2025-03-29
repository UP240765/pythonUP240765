import random as rd
import string as st
fruits = ["manzana", "plátano", "naranja", "uva", "sandía", "pera", "kiwi", "mango", "fresa", "cereza"]


#Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(lt):
    rd.shuffle(lt)
    return lt

#Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def unique_nums():
    nums = set()
    while len(nums) <= 7:
        x = rd.randint(0,len(st.digits)-1)
        nums.add(st.digits[x])
    return nums

print(unique_nums())