# -*- coding: utf-8 -*-

import pytest
from tennis1 import TennisGame1
from tennis2 import TennisGame2
from tennis3 import TennisGame3
from tennis4 import TennisGame4
from tennis5 import TennisGame5
from tennis6 import TennisGame6

from tennis_unittest import test_cases, play_game, play_game_translate


def test_of_default():
    game1 = play_game_translate(TennisGame1, 0, 0, "player1", "p2", "fr")
    game1_score = game1.score()
    game2 = play_game_translate(TennisGame1, 0, 0, "p1", "player2", "fr")
    game2_score = game2.score()
    game3 = play_game_translate(TennisGame1, 0, 0, "player1", "player2", "fr")
    game3_score = game3.score()
    assert game1_score == game2_score == game3_score

@pytest.mark.parametrize('p1Points p2Points score p1Name p2Name'.split(), test_cases)
def test_get_score_game1(p1Points, p2Points, score, p1Name, p2Name):
    game = play_game_translate(TennisGame1, p1Points, p2Points, p1Name, p2Name, 'en')
    assert score == game.score()