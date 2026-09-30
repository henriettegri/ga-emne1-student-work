class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1

first_pet = Pet("Luna", 3)
second_pet = Pet("Milo", 5)
first_pet.birthday()
print(first_pet.age)
print(second_pet.age)