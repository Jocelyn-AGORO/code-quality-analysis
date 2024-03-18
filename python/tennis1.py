from typing import Dict

from internationalize import translate, translate_parameterized

class TennisGame1:

    SCORE_STEPS = ["Love", "Fifteen", "Thirty", "Forty"]
    def __init__(self, player1_name, player2_name, language):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.language = language

    def won_point(self, playerName: str):
        if playerName == self.player1_name:
            self.player1_score += 1
        elif playerName == self.player2_name:
            self.player2_score += 1
        else:
            raise ValueError(self.translate_parameterized("playerNameError", {playerName: playerName}))

    def translate(self, key: str):
        return translate(self.language, key)

    def translate_parameterized(self, key: str, kwargs: Dict):
        return translate_parameterized(self.language, key,**kwargs)

    def score(self):
        if self._is_score_tied():
            return self._score_when_tied()
        elif self._is_advantage_or_win():
            return self._score_advantage_or_win()
        else:
            return self._normal_score()

    def _is_score_tied(self):
        # Simplification de la vérification des scores égaux.
        return self.player1_score == self.player2_score

    def _score_when_tied(self):
        # Centralisation du mapping des scores pour un score égal dans une méthode dédiée.
        # Cela améliore la clarté et facilite les modifications futures.
        if self.player1_score < 3 :
            step = self.translate(self.SCORE_STEPS[self.player1_score].lower())
            alls = self.translate("all")
            print(step)
            return f"{step}-{alls}"
        else:
            return translate(self.language, "deuce")
        # return f"{step}-{alls}" if self.player1_score < 3 else

    def _is_advantage_or_win(self):
        # Vérification simplifiée pour déterminer si l'un des joueurs a l'avantage ou a gagné.
        return self.player1_score >= 4 or self.player2_score >= 4

    def _score_advantage_or_win(self):
        score_difference = self.player1_score - self.player2_score
        if score_difference == 1:
            return f"{self.translate('advantage')} " + self.player1_name
        elif score_difference == -1:
            return f"{self.translate('advantage')} " + self.player2_name
        elif score_difference >= 2:
            return f"{self.translate('win')} {self.translate('for')} " + self.player1_name
        else:
            return f"{self.translate('win')} {self.translate('for')} " + self.player2_name

    def _normal_score(self):
        # Remplacement du mapping des scores par une séquence explicite, pour une lecture et une maintenance facilitées.
        player1_step = self.SCORE_STEPS[self.player1_score]
        player2_step = self.SCORE_STEPS[self.player2_score]
        return f"{self.translate(player1_step)}-{self.translate(player2_step)}"
