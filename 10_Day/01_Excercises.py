#Iterate 0 to 10 using for loop, do the same using while loop.
for i in range (-1,11,1):
    print(f"For loop: {i}")

x = 0
while x != 11:
    print(f"While loop: {x}")
    x = x+1

#Iterate 10 to 0 using for loop, do the same using while loop.

for i in range (10,0,-1):
    print(f"For loop: {i}")

x = 10
while x != -1:
    print(f"While loop: {x}")
    x = x-1

#Write a loop that makes seven calls to print(), so we get on the output the following triangle:
for i in range (0,8,1):
    print(f"#"*i)

#Use nested loops to create the following:
for i in range(8):
    for x in range(8):
        print(f"#", end=f" ")
    print()

#Print the following pattern:
for i in range(11):
    print(f"{i} x {i} = {i**2}")

#Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
libraries = ['Python', 'Numpy','Pandas','Django', 'Flask']

i = 0
for lib in libraries:
    print(f"Element {i}: {lib}")
    i = i + 1

#Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(0,101,1):
    if i % 2 == 0:
        print(i)

#Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(0,101,1):
    if i % 2 != 0:
        print(i)



