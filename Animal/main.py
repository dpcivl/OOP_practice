from Zoo import Zoo
from Lion import Lion
from Elephant import Elephant
from Penguin import Penguin

zoo = Zoo()
peter = Lion()
gaze = Penguin()
larg = Elephant()


zoo.addAnimal(peter)
zoo.addAnimal(gaze)

print(zoo.makeAllSounds())

zoo.addAnimal(larg)

print(zoo.makeAllSounds())

print(larg.move())