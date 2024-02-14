from GameFrame import RoomObject, Globals
import random

class Zork(RoomObject):
    """
    A class for the game's antagonist
    """
    def __init__(self, room, x, y):
        """
        Initialise the boss object
        """
        # include attributes and methods from room object
        RoomObject.__init__(self, room, x, y)

        # set image
        image = self.load_image("Zork.png")
        self.set_image(image,135,165)

        # set inital movement
        self.y_speed = random.choice([-10, 10])
    
    def keep_in_room(self):
        """
        Keeps the Zork inside the top and bottom room limits
        """
        if self.y < 0 or self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y_speed *= -1

    def step(self):
        """
        Determine what happens to the Dragon on each tick of the game clock
        """
        self.keep_in_room()