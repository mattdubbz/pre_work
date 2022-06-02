foods = ('potatoes', 'beef', 'carrots', 'bananas', 'chicken')
for food in foods:
    print(food)
try:
    foods[0] = 'rice'
except Exception as e:
    print(e)
foods = ('potatoes', 'beef', 'carrots', 'dumplings', 'sushi')
for food in foods:
    print(food)
