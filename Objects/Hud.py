from GameFrame import TextObject, Globals

class Score(TextObject):
    """
    A class for displaying the current score
    """
    def __init__(self, room, x: int, y: int, text=None):
        """
        Initialise the score object
        """
        # include attributes and methods from text object
        TextObject.__init__(self, room, x, y, text)

        # set values
        self.size = 60
        self.font = 'Arial Black'
        self.colour = (225,225,225)
        self.bold = False
        self.update_text()

    def update_score(self, change):
        """
        updates the score and redraws the text
        """
        Globals.SCORE += change
        self.text = str(Globals.SCORE)
        self.update_text()