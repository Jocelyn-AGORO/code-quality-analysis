# -*- coding: utf-8 -*-

import pytest
from tennis1 import TennisGame1

from tennis_unit_test import test_cases, play_game_translate


def test_of_default():
    """Default test"""
    game1 = play_game_translate(TennisGame1, 0, 0, "player1", "p2", "fr")
    game1_score = game1.score()
    game2 = play_game_translate(TennisGame1, 0, 0, "p1", "player2", "fr")
    game2_score = game2.score()
    game3 = play_game_translate(TennisGame1, 0, 0, "player1", "player2", "fr")
    game3_score = game3.score()
    assert game1_score == game2_score == game3_score

@pytest.mark.parametrize('p1_points p2_points score p1_name p2_name'.split(), test_cases)
def test_get_score_game1(p1_points, p2_points, score, p1_name, p2_name):
    """Test 1"""
    game = play_game_translate(TennisGame1, p1_points, p2_points, p1_name, p2_name, 'en')
    assert score == game.score()