crazy_list = [1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
print(crazy_list[3][1][2][0])

animals = ['Lion', 'Tiger', 'Elephant', 'Giraffe', 'Cheetah']

# key concepts:
# sequential versus random access
# (new terms, not new concepts)

for animal in animals:
    print(animal)

print(animals[2])

for animal in animals:
    if animal == 'Zebra':
        in_zebra = True
        break

    else:
        in_zebra = False

print(f"Zebra is in animals: ", in_zebra)

#Other way
try:
    animals.index('Zebra')
except ValueError:
    print("No Zebras found")

# Best
print("Has Zebra", "Zebra" in animals)

print("Is giraffe in 2?" , animals[2] == "giraffe")

animals.append("Zebra")
animals.remove("Cheetah")

animals = tuple(animals)
#animals.append('Bear')  #This occurs error 'AtributeError: 'tuple' object has no attribute 'append''


# Challenges 2
# Build a list of characteristics and a list of animals, and then use the two lists to create a dictionary of animals and their characteristic. Try using zip; try using a list comprehension.
animals_dict = {'Lion': 'Brave', 'Tiger': 'Fierce', 'Elephant': 'Large', 'Giraffe': 'Tall', 'Zebra': 'Striped'}


animal_names = []
for name in animals_dict:
    animal_names.append(name)


# better (but identical):
animal_names = [name for name in animals_dict]


animal_characteristics = []

#Built a list of animals
animal_names = list(animals_dict.keys())

#Built a list of characteristics
animal_characteristics = list(animals_dict.values())

for value in animals_dict.values():
    animal_characteristics.append(value)

animal_characteristics = [value for value in animals_dict.values()]

#Create a dictionary of animals and their characteristic
animals = {}

for n, c in zip(animal_names, animal_characteristics):
    animals[n] = c

# better (but same)
animals = {n:c for n, c in zip(animal_names, animal_characteristics)}
print(animals)

# or as a comprehension:

class Animal:
    def __init__(self, name, characteristic):
        self.name = name
        self.characteristic = characteristic

    def modify_characteristics(self, new_characteristic):
        self.characteristic = new_characteristic

#Create an instance of Animal class
lion = Animal('Lion','King')

## For review and test during for week 2
lion.modify_characteristics('Brave')

#Create an empty dictionary
animal_classes ={}

for key, value in animals.items():
    animal_classes[key] = Animal(key, value)

animal_classes = [Animal(a, c)
                   for a,c in animals.items()]

print(animal_classes)




#What is zip function?
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)
#use the tuple() function to display a readable version of the result:
print(tuple(x))

#Output : (('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))