# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

print(f"The lenght of it companies is {len(it_companies)}")

it_companies.add("Twitter")
print(it_companies)

it_companies.update(["Youtube","Linux","Opera"])
print(it_companies)

it_companies.discard("Youtube")
print(it_companies)

print(f"La diferencia entre discard() y remove es que remove no indica error si no encuentra el elemento en cambio remove() si indica error")
