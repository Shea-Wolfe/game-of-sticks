import unittest
from sticks import *

good_entry = 2
bad_entry = 5

class Teststicks(unittest.TestCase):

    def test_player_move_true(self):
        self.assertEqual(player_move(5, 2), 3)
    def test_player_move_false(self):
        self.assertFalse(player_move(5,2) == 5)



if __name__ == '__main__':
    unittest.main()
