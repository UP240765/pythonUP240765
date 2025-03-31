#Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
numNeg = [i for i in numbers if i <= 0]
print(numNeg)

#Flatten the following list of lists of lists to a one dimensional list
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [ number for row in list_of_lists for number in row]
flattened_list2 = [ number for row in flattened_list for number in row]
print(flattened_list2)

#Using list comprehension create the following list of tuples
tuples = [(i,1, i**1 ,i**2,i**3,i**4,i**5,) for i in range(11)]
print(tuples)

#Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries = [[country.upper(), country[:3].upper(), capital.upper()] 
                       for sublist in countries for (country, capital) in sublist]
print(flattened_countries)

#Change the following list(countries) to a list of dictionaries:
dicctionary_countries = [{'country':country.upper(),'city':city.upper()} for sublist in countries 
                         for (country,city) in sublist]
print(dicctionary_countries)

#Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_name = [[name + " " + lastname] for sublist in names for (name,lastname) in sublist]
full_name = [i for n in full_name for i in n]
print(full_name)

#Write a lambda function which can solve a slope or y-intercept of linear functions.
slope = lambda x1,y1,x2,y2 : (y2-y1)/(x2-x1)
print(slope(3,5,4,1))

