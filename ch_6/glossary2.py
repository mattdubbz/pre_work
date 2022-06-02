glossary = {
    "key": "dictionary",
    "list": "storage",
    "tuple": "immutable",
    "loop": "processing",
    "if": "check",
    "if": "again",
}

for key, value in glossary.items():
    print(f"Key: {key}")
    print(f"Value: {value}\n")
    
for key in glossary:
    print(key)
    
print("==========")

for key in sorted(glossary.keys()):
    print(key)

print("==========")

for val in sorted(glossary.values()):
    print(val)

for key in set(glossary.keys()):
    print(f"Unique keys: {key}")
