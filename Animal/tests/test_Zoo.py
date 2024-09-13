import unittest
from Zoo import Zoo
from Lion import Lion
from Elephant import Elephant
from Penguin import Penguin

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()
        self.lion = Lion()
        self.elephant = Elephant()
        self.penguin = Penguin()

    def test_addAnimal(self):
        self.zoo.addAnimal(self.lion)
        self.assertEqual(self.zoo.animals, [self.lion])
    
    def test_makeAllSounds(self):
        self.zoo.addAnimal(self.lion)
        self.zoo.addAnimal(self.elephant)
        self.zoo.addAnimal(self.penguin)
        self.assertEqual(self.zoo.makeAllSounds(), "Grrrr\nBboooooooo\nBeeeeeh\n")