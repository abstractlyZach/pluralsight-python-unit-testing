import pytest

import tennis

test_cases = (
    ('expected_score', 'points', 'comment'),
    [
        ('love-all', (0, 0), 'early game, scores equal'),
        ('fifteen-all', (1, 1), 'early game, scores equal'),
        ('thirty-all', (2, 2), 'early game, scores equal'),
        ('fifteen-love', (1, 0), 'early game, scores uneven'),
        ('thirty-fifteen', (2, 1), 'early game, scores uneven'),
        ('forty-thirty', (3, 2), 'early game, scores uneven'),
        ('love-forty', (0, 3), 'early game, scores uneven'),
        ('deuce', (3, 3), 'endgame with even scores'),
        ('deuce', (5, 5), 'endgame with even scores'),
        ('deuce', (50, 50), 'endgame with even scores')
    ]
)

@pytest.mark.parametrize(*test_cases)
def test_scores(expected_score, points, comment):
    assert expected_score == tennis.tennis_score(*points)


