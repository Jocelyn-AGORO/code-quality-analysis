import unittest

from tennis1 import TennisGame1


class GoldenMasterTest(unittest.TestCase):
    """Class test golden master de tests d'urgence"""

    DIR = ".\\golden_master"

    @staticmethod
    def play_game(p1_name, p2_name, p1_points, p2_points,  lang):
        """Method that plays a game for each test case"""
        game = TennisGame1(p1_name, p2_name, lang)
        for i in range(max(p1_points, p2_points)):
            if i < p1_points:
                game.won_point(p1_name)
            if i < p2_points:
                game.won_point(p2_name)
        return game.score()

    def make_file_name(self, score_player_1, score_player_2, lang):
        """Method that creates a file for each golden master test case"""
        return f"{self.DIR}\\{lang}\\{score_player_1}_{score_player_2}.txt"

    def test_record(self):
        """Record method"""
        for language in ["fr", "en"]:
            for score_player_1 in list(range(0, 16)):
                for score_player_2 in list(range(0, 16)):
                    with self.subTest(f"{score_player_1}, {score_player_2}"):
                        sortie = self.play_game("player1", "player2", score_player_1, score_player_2, language)
                        file = open(self.make_file_name(score_player_1, score_player_2, language), "w", encoding="utf-8")
                        file.writelines(sortie)
                        file.close()

    def _test_replay(self):
        """Replay method"""
        for language in ["fr", "en"]:
            for score_player_1 in list(range(0, 16)):
                for score_player_2 in list(range(0, 16)):
                    with self.subTest(f"{score_player_1}, {score_player_2}"):
                        sortie = self.play_game(score_player_1, score_player_2, "player1", "player2", language)
                        file = open(self.make_file_name(score_player_1, score_player_2, language), "r", encoding="utf-8")
                        attendu = file.read()
                        file.close()
                        self.assertEqual(attendu, sortie)
