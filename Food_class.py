import pygame
import random

from Snake_class import *

"""Our second class is food class. This class contains objects that the functionalities of our food. 
For instance, we need to place our food to different positions whenever our game reset. This class also 
draw our rectangle(food) object in the surface of our game screen. This class also relates to the other
 classes as it does only display our food on the screen but also position it randomly."""


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = (223, 163, 49)
        self.randomize_position()


    def randomize_position(self):
        self.position = (random.randint(0, grid_width - 1) * gridsize, random.randint(0, grid_height - 1) * gridsize)
'''Pseudo Code 1: Self.position is set to a formulae inorder to randomly position our snake.'''

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (gridsize, gridsize))
        pygame.draw.rect(surface, self.color, r)
'''Pseudo Code 2: r is assign to pygame.Rect which display our food in rectangle
 And gives specific color to the rectangle which is our food.
#Whenever this object is called, it display the rectangle with specific color and set position.'''


def drawGrid(surface):
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            if (x + y) % 2 == 0:
                r = pygame.Rect((x * gridsize, y * gridsize), (gridsize, gridsize))
                pygame.draw.rect(surface, (93, 216, 228), r)
            else:
                rr = pygame.Rect((x * gridsize, y * gridsize), (gridsize, gridsize))
                pygame.draw.rect(surface, (84, 194, 205), rr)

'''Pseudocode 3. This method whenever called will draw our rectangle on the surface.
We do this by getting the exact size of our rectangle that is place in our screen.
#It does this by creating a 'for loop'.'''