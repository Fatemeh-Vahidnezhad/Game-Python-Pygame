from constants import *
import pygame
from fruit import *
from Deck import *
import random


class Board:
    def __init__(self, window):
        self.window = window   
        self.grid = [[None for _ in range(row_col_num[1])] for _ in range(row_col_num[0])]



    def draw(self):
        # cnt = 0
        for row in range(row_col_num[0]):
            for col in range(row_col_num[1]):
                # cnt += 1
                x = col * cell_size[0] + board_loc[0]
                y = row * cell_size[1] + board_loc[1]
                # print('x,y::', x, y)
                pygame.draw.rect(self.window, (255, 255, 255), (x, y, cell_size[0], cell_size[1]), 2)  # 2 is the border thickness
                


#                             ---------------------test the code -------------------------
# if __name__ == '__main__':
#     import pygame
#     import sys

#     window_width = 1000
#     window_height = 800
#     BLACK = (0, 0, 0)

#     pygame.init()
#     window = pygame.display.set_mode((window_width, window_height))
#     clock = pygame.time.Clock()

#     oboard = Board(window)
#     # oboard.swap((0,0), (1,0))

#     while True:
#         for event in pygame.event.get():
#             if (event.type == pygame.QUIT):
#                 pygame.quit()
#                 sys.exit()

#     # Clear the screen
#         window.fill((0, 0, 0))

#         oboard.draw()
#         # oboard.draw_fruits()
#         pygame.display.update()
#         clock.tick(30) 
      
        