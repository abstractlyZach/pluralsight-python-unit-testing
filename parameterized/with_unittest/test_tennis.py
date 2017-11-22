import unittest

import tennis


class TestTennis(unittest.TestCase):
    # can remove the two "test_..." cases
    def test_uneven_scores_early_game(self):
        self.assertTrue(tennis.tennis_score(0, 1) == 'love-fifteen')
        self.assertTrue(tennis.tennis_score(1, 0) == 'fifteen-love')
        self.assertTrue(tennis.tennis_score(3, 1) == 'forty-fifteen')
        self.assertTrue(tennis.tennis_score(2, 3) == 'thirty-forty')

    def test_even_scores_early_game(self):
        self.assertTrue(tennis.tennis_score(0, 0) == 'love-all')
        self.assertTrue(tennis.tennis_score(2, 2) == 'thirty-all')

    def assert_tennis_score(self, expected_score, points):
        player1_points, player2_points = points
        actual_score = tennis.tennis_score(player1_points, player2_points)
        self.assertTrue(expected_score == actual_score)


test_case_data = {
    'even_scores':
        [
            ('love-all', (0, 0)),
            ('fifteen-all', (1, 1)),
            ('thirty-all', (2, 2))
        ],
    'uneven_scores':
        [
            ('love-fifteen', (0, 1)),
            ('fifteen-love', (1, 0)),
            ('thirty-forty', (2, 3)),
            ('forty-fifteen', (3, 1))
        ]
}

def test_tennis_template(*args):
    def template(self):
        self.assert_tennis_score(*args)
    return template


for behavior, test_data in test_case_data.items():
    for test_info in test_data:
        custom_test = test_tennis_template(*test_info)
        points = test_info[1]
        test_name = 'test_{}_{}_{}'.format(behavior, points[0], points[1])
        setattr(TestTennis, test_name, custom_test)


