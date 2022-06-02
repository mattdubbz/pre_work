boomer = {'name': 'Boomer', 'kind': 'dog', 'owner': 'Matt'}
lucy = {'name': 'Lucy', 'kind': 'dog', 'owner': 'Jess'}
benito = {'name': 'Benito', 'kind': 'parrot', 'owner': 'Maria'}
julio = {'name': 'Julio', 'kind': 'cat', 'owner': 'Jerry'}

pets = [boomer, lucy, benito, julio]

for pet in pets:
    print(f"Pet's name: {pet['name']}")
    print(f"Pet's kind: {pet['kind']}")
    print(f"Pet's owner: {pet['owner']}")
    print("======================")
