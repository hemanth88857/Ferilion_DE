

class pet :

    def __init__(self,name,age,species):
        self.name = name
        self.age = age
        self.species = species

    def display_info(self):

        return f"Name : {self.name} , age : {self.age} , species : {self.species})"


    def make_Sound(self):
        return "pet makes sounds"

    def feed(self):
        return f"{self.species} like milk"

    def species_details(self):
        return self.species


class dog(pet):

    def make_Sound(self,species):
        return f"{species}  sound as brak"


    def feed(self):
        return  " dog eat Egg"



animal = pet("kan","3","dog")

print(animal.name)

doberman = dog("manis","4","dog")
doberman.make_Sound(animal.name)
print(doberman.make_Sound(animal.species_details()))

print(super(dog,doberman).make_Sound())

# print(dog.super.make_Sound)
