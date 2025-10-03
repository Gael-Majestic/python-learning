people = ['Conrad', 'Deepak', 'Heinrich', 'Tom']
ages = [29, 30, 34, 36]
for person in people:
    print(f'{person} is {ages[people.index(person)]} years old')