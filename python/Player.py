class Player:
    """Class that represents a player"""
    def __init__(self, name, score=0):
        self.name = name
        self.score = score
        
    def get_name(self):
        return self.name