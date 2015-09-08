import unittest
from ai_sticks import *


class Teststicks(unittest.TestCase):

    def test_player_move_true(self):
        self.assertEqual(player_move(5, 2), 3)
    def test_player_move_false(self):
        self.assertFalse(player_move(5,2) == 5)
    def test_ai_dict(self):
        self.assertTrue(2 in get_ai_dict()[5])


if __name__ == '__main__':
    unittest.main()
