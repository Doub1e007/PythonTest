dict1 = {'name': 'Tom', 'age': 18, 'gender': 'male'}

for key in dict1.keys():
    print(key,end=' ')

print()

for value in dict1.values():
    print(value,end=' ')

print()

for item in dict1.items():
    print(item,end=' ')

print()

for key,value in dict1.items():
    print(f'{key} = {value}',end=' ')
