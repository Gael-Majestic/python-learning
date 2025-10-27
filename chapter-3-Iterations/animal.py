# Nested Loops Example: Animal Purchases
animals = ['cat', 'dog', 'horse', 'kiwi']
for first_animal in animals:
    for second_animal in animals:
        print('yesterday I bought a %s. Today I bought a %s.' % (first_animal, second_animal))