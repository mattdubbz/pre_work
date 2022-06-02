pizzas = ['cheese', 'extra cheese', 'pepperoni', 'supreme', 'banana pepper']
friend_pizzas = pizzas[:]
pizzas.append('anchoves')
friend_pizzas.append('olives')
print("my favorite pizzas are:")
for pizza in pizzas:
    print("\t", pizza)
print()
print("My friends favorit pizzas are:")
for pizza in friend_pizzas:
    print("\t", pizza)