

#Define a Python function which is "Conway's Game Of Life".
#Set field size to 800x600 and cell size to 10x10. Randomize the startup cells.
#Display game field using pygame library.

import pygame
import random

#Define a class for the game field.
class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.field = []
        for i in range(self.height):
            self.field.append([])
            for j in range(self.width):
                self.field[i].append(random.randint(0, 1))

    def get_cell(self, x, y):
        return self.field[y][x]

    def set_cell(self, x, y, state):
        self.field[y][x] = state

    def get_neighbours(self, x, y):
        neighbours = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i == 0 and j == 0) or (x + i < 0) or (y + j < 0) or (x + i >= self.width) or (y + j >= self.height):
                    continue
                neighbours.append(self.get_cell(x + i, y + j))
        return neighbours

    def get_next_generation(self):
        new_field = Field(self.width, self.height)
        for i in range(self.height):
            for j in range(self.width):
                neighbours = self.get_neighbours(j, i)
                if self.get_cell(j, i) == 1:
                    if sum(neighbours) in [2, 3]:
                        new_field.set_cell(j, i, 1)
                    else:
                        new_field.set_cell(j, i, 0)
                else:
                    if sum(neighbours) == 3:
                        new_field.set_cell(j, i, 1)
                    else:
                        new_field.set_cell(j, i, 0)
        return new_field

    def draw(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                if self.get_cell(j, i) == 1:
                    pygame.draw.rect(screen, (255, 255, 255), (j * 10, i * 10, 10, 10))
                else:
                    pygame.draw.rect(screen, (0, 0, 0), (j * 10, i * 10, 10, 10))

#Initialize pygame library.
pygame.init()

#Create a window with size 800x600.
screen = pygame.display.set_mode((800, 600))

#Create a game field with size 800x600 and randomize the cells.
field = Field(800 // 10, 600 // 10)

#Main loop.
while True:
    #Check for events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    #Draw the game field.
    field.draw(screen)

    #Update the game field.
    field = field.get_next_generation()

    #Update the screen.
    pygame.display.flip()


