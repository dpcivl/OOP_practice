import unittest
from Lion import Lion
from Elephant import Elephant
from Penguin import Penguin

class TestAnimal(unittest.TestCase):
    def setUp(self):
        self.lion = Lion()
        self.elephant = Elephant()
        self.penguin = Penguin()

    def test_makeSound(self):
        self.assertEqual(self.lion.makeSound(), "Grrrr\n")
        self.assertEqual(self.elephant.makeSound(), "Bboooooooo\n")
        self.assertEqual(self.penguin.makeSound(), "Beeeeeh\n")

    def test_move(self):
        self.assertEqual(self.lion.move(), "사자가 움직인다!")
        self.assertEqual(self.elephant.move(), "끼리끼리 코끼리~")
        self.assertEqual(self.penguin.move(), "펭귄이 움직였다!")