import unittest
from ai_sticks import *
ai_dict = {key: [1,2,3] for key in range(1,101)}

class Teststicks(unittest.TestCase):

    def test_dual_ai_dict_changes_true(self):
        self.assertEqual(dual_ai_dict_changes({1:[1,2,3],2:[1,2,3,3],3:[1,2,3]}, {2:3}, {3:1}, True), {1:[1,2,3],2:[1,2,3],3:[1,2,3,1]})

    def test_dual_ai_dict_changes_false(self):
        self.assertFalse(dual_ai_dict_changes(ai_dict, {1:1, 5:3}, {3:2, 8:3}, True)[8] ==[1,2,3])

    def test_player_move_true(self):
        self.assertEqual(player_move(5, 2), 3)

    def test_player_move_false(self):
        self.assertFalse(player_move(5,2) == 5)

    def test_ai_dict(self):
        self.assertTrue(2 in get_ai_dict()[5])

    def test_ai_dict_changes_win_true(self):
        self.assertTrue((ai_dict_changes(ai_dict, {2:1,5:3}, True)[5]) == [1, 2, 3, 3])

    def test_ai_dict_changes_lose_false(self):
        self.assertFalse((ai_dict_changes(ai_dict, {2: 1, 5:3}, False)[5]) == [1,2,3,3])

    def test_ai_dict_changes_lose_true(self):
        self.assertTrue((ai_dict_changes(ai_dict, {2: 1, 5:3}, False)[5]) == [1,2,3])

    def test_ai_turn_true(self):
        self.assertTrue(ai_turn(ai_dict, 10, {})[0] in [1,2,3])


if __name__ == '__main__':
    unittest.main()
