import pygame 
from constants import *

class Score:
    def __init__(self, window):
        self.window = window
        file_name = 'images/dimond.png'
        self.image = pygame.image.load(file_name)
        self.score_p1 = 0
        self.score_p2 = 0
        self.font = pygame.font.Font(None, 30)


    def draw_p1(self):
        self.window.blit( self.image, (10, 30)) 

        #show score
        score_text = self.font.render("Score of player 1: {}".format(self.score_p1), True, WHITE)
        self.window.blit(score_text, (50, 180))
    
    
    def draw_p2(self):

        score_text_p2 = self.font.render("Score of Player 2: {}".format(self.score_p2), True, WHITE)
        self.window.blit(score_text_p2, (50, 200))


    def compute_score_p1(self):
        self.score_p1 += 10
        self.draw_p1()

    def compute_score_p2(self):
        self.score_p2 += 10
        print('score AI,', self.score_p2)
        self.draw_p2()


    def final_score(self):
        return self.score_p1
    
    def final_score_p2(self):
        return self.score_p2