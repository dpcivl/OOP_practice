from abc import abstractmethod

class Animal:
    def __init__(self):
        name = ""
        age = 0
        species = None
        
    @abstractmethod
    def makeSound(self):
        pass

    def move(self):
        print("움직입니다.")