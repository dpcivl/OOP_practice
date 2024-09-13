class Zoo:
    def __init__(self, name="IlGwang"):
        self.animals = []
        self.name = name

        print(f"Welcome to the Zoo {self.name}")

    def addAnimal(self, animal):
        self.animals.append(animal)

    def makeAllSounds(self):
        output = ""
        for animal in self.animals:
            output += animal.makeSound()
        
        return output