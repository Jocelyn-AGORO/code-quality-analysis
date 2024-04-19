class Player:
    """Class that represents a player"""
    def __init__(self, name, score=0):
        self.name = name
        self.score = score
    
    def get_name(self):
        """Getter for the player name"""
        return self.name
    
    def get_score(self):
        """Getter for the player score"""
        return self.score
    
    def win_point(self):
        """Getter for the player score"""
        self.score += 1