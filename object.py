from parameters import *


class Object:
    def __init__(self, x, y, width, speed, image):
        self.x = x
        self.y = y
        self.width = width
        self.speed = speed
        self.image = image

    def move(self):
        if self.x >= -self.width:
            display.blit(self.image, (self.x, self.y))
            self.x -= self.speed
            return True
        else:
            return False

    def return_self(self, radius, y, width, image):
        self.y = y
        self.width = width
        self.image = image
        self.x = radius
        display.blit(self.image, (self.x, self.y))

