import math

#Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(n1,n2):
    sum = n1 + n2
    return sum

#Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def circle_area(r):
    area = math.pi*r**2
    return area

#Write a function called add_all_nums
def add_all_nums(nums):
    sum = 0
    if type(nums) == list:
        for num in nums:
            if type(num) == int:
                sum += num
            else:
                return f"One element in the list is not a number"
    else:
        if type(nums) == int:
                return
        else:
            return f"One element in the list is not a number"
    return sum

#Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def temperatureCF(cel):
    far = (cel * 9/5) + 32
    return far

#Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    if month == "SEPTEMBER" or month == "OCTOBER" or month == "NOVEMBER":
        return f"The current season is Autumn"

    elif month == "DECEMBER" or month == "JANUARY" or month == "FEBRUARY":
        return f"The current season is Winter"

    elif month == "MARCH" or month == "APRIL" or month == "MAY":
        return f"The current season is Spring"

    elif month == "JUNE" or month == "JULY" or month == "AUGUST":
        return f"The current season is Summer"
    else:
        return f"Invalid Data"
    
#Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1,x2,y1,y2):
    slope = (y2+y1)/(x2-x1)
    return slope

#Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a,b,c):
    if b**2 - 4*a*c >= 0:
        sol1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
        sol2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
    else:
        return "The ecuation don't have any real solution"
    return sol1, sol2

#Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lis):
    if type(lis) == list:
        for i in lis:
            print(i)
    else:
        return f"{lis} is not a list"
    
#Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):  # Looping backward
        reversed_arr.append(arr[i])
    return reversed_arr

#Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
capItems = []
def capitalize_list_items(li):
    if type(li) == list:
        for l in li:
            x = l.capitalize()
            capItems.append(x)
    else:
        return f"{li} is not a list"
    return capItems

#Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
fruits = ["apple", "banana", "cherry"]
def add_item(li,item):
    li.append(item)
    return li

#Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(li,item):
    if item in li:
        li.remove(item)
    else:
        return f"{item} is not in the list"
    return li

#Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(num):
    sum = 0
    for i in range(num+1):
        sum += i
    return sum

#Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
sumOdd = 0
def sum_of_odds(num):
    for i in range(num+1):
        if i % 2 != 0:
            sumOdd += i
    return sumOdd

#Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that range.
sumEven = 0
def sum_of_even(num):
    for i in range(num+1):
        if i % 2 == 0:
            sumEven += i
    return sumEven

