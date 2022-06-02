cubes = [num**3 for num in range(1, 11)]
for num in cubes:
    print(num)
print("The first 3 items are", cubes[:3])
print("3 items from the middle are", cubes[3:7])
print("The last 3 items are", cubes[-3:])