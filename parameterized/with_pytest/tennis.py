scores = ['love', 'fifteen', 'thirty', 'forty']

def tennis_score(player1_points, player2_points):
    if player1_points == player2_points:
        return _matching_score(player1_points)
    else:
        return _not_matching_score(player1_points, player2_points)

def _matching_score(points):
    if points > 2:
        return 'deuce'
    else:
        return '{}-all'.format(scores[points])

def _not_matching_score(player1_points, player2_points):
    player1_score = scores[player1_points]
    player2_score = scores[player2_points]
    return '{}-{}'.format(player1_score, player2_score)
