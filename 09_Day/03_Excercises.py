person = {
    'first_name': 'Ann',
    'last_name': 'Kiraman',
    'age': 250,
    'country': 'England',
    'is_marred': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Baker Street',
        'zipcode': '02210'
    }
}

#Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person.keys():
    mid = int(len(person['skills'])/2)
    print(person['skills'][mid])
else:
    print(f"'skills' is not on the person")

#Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person.keys():
    if "Python" in person['skills']:
        print(f"Python is a skill in the diccionary")
    else:
        print(f"Python is not a skill in the diccionary")
else:
    print(f"'skills' is not on the person")