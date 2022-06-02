glossary = {
    "key": "dictionary",
    "list": "storage",
    "tuple": "immutable",
    "loop": "processing",
    "if": "check",
}
for key in glossary:
    print(f"Key: {key}")
    print(f"Value: {glossary[key]}\n")

for key, value in glossary.items():
    print(f"Key: {key}")
    print(f"Value: {value}\n")

for key in glossary.keys():
    print(key)

keys = glossary.keys()
print(type(keys))

for key in sorted(glossary.keys()):
    print(key)

for value in glossary.values():
    print(value)

print(set(glossary))
