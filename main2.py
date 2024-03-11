import pygame 
from pygame.locals import *
import sys
import pygwidgets
# import pyghelpers
import time 
from constants import *
from board1 import *
from score import *
from player import *
from game1 import *
from time1 import *
from message import *



class GameManager:
    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode((window_width, window_height))
        self.clock = pygame.time.Clock()
        self.winnerSound = pygame.mixer.Sound("sounds/ding.wav")
        # self.font = pygame.font.Font(None, 24)

        self.game_over = False

        # define objects
        self.otime = Time(self.window)
        self.oscore = Score(self.window)
        self.oboard = Board(self.window)
        self.oplayer = Player(self.window)
        self.ogame = Game(self.window)
        self.omessage = MessageManager(self.window)
        
        # switch images
        # loc1
        self.grid_x = 0
        self.grid_y = 0

        #loc2:
        self.x = 0
        self.y = 0
        

    def handle_mouse_click(self,loc):
        i, j = loc
        grid_x = (i- board_loc[0]) // (cell_size[1])
        grid_y = (j- board_loc[1]) // (cell_size[0])

        if 0 <= grid_x < row_col_num[1] and 0 <= grid_y < row_col_num[0]:
            self.grid_x = grid_x
            self.grid_y = grid_y


    def handle_mouse_release(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        x = (mouse_x - board_loc[0]) // cell_size[0]
        y = (mouse_y - board_loc[1]) // cell_size[1]
        if 0 <= x < row_col_num[1] and 0 <= y < row_col_num[0]:
            self.x = x
            self.y = y    

    def handle_events(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or \
                ((event.type == KEYDOWN) and (event.key == K_ESCAPE)):
                self.game_over = True  

            elif self.oplayer.player_status():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 or event.button == 3:
                        self.handle_mouse_click((event.pos[0], event.pos[1]))

                elif event.type == pygame.MOUSEBUTTONUP:
                    self.handle_mouse_release()
                    if 0 <= self.grid_y <= 3 and 0<=self.grid_x<=3 and 0 <= self.x <= 3 and  0 <= self.y <= 3:
                        index1 = self.grid_y * row_col_num[0] + self.grid_x
                        index2 = self.y * row_col_num[0] + self.x

                        Index = self.ogame.swap(index1, index2)
                        if self.ogame.check_similar_in_a_row(Index):
                            self.oscore.compute_score_p1()
                            # self.ogame.replace_image(index)
                            self.winnerSound.play()
                            self.oplayer.switch_player()
                            self.omessage.display_message('player 2 turns!', (30, 450))
                        else:
                            self.oplayer.switch_player()
                            self.omessage.display_message('player 2 turns!', (30, 450))

            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 or event.button == 3:
                        self.handle_mouse_click((event.pos[0], event.pos[1]))

                elif event.type == pygame.MOUSEBUTTONUP:
                    self.handle_mouse_release()
                    if 0 <= self.grid_y <= 3 and 0<=self.grid_x<=3 and 0 <= self.x <= 3 and  0 <= self.y <= 3:
                        index1 = self.grid_y * row_col_num[0] + self.grid_x
                        index2 = self.y * row_col_num[0] + self.x

                        Index = self.ogame.swap(index1, index2)
                        if self.ogame.check_similar_in_a_row(Index):
                            self.oscore.compute_score_p2()
                            self.winnerSound.play()
                            self.oplayer.switch_player()
                            self.omessage.display_message('player 1 turns!', (30, 450))
                        else:
                            self.oplayer.switch_player()
                            self.omessage.display_message('player 1 turns!', (30, 450))

    def update(self):
        if self.otime.is_expired():
            self.omessage.display_message('Game Over - Time Expired', (window_width // 2, (window_height // 2)+ 100 ))
            if self.winner() == 'player 1':
                print('player 1 won the game!')
                self.omessage.display_message('Player 1 is winner!', (window_width // 2, (window_height // 2)+ 120 ))

            elif self.winner() == 'player 2':
                print('player 2 won the game!')
                self.omessage.display_message('Player 2 is winner!', (window_width // 2, (window_height // 2)+ 120 ))

            else: 
                print('It is a tie!')
                self.omessage.display_message('It is a tie!', (window_width // 2, (window_height // 2)+ 120 ))

            time.sleep(5)
            self.game_over = True  

   
    def winner(self):
        if self.oscore.final_score() > self.oscore.final_score_p2():
            return 'player 1'
        elif self.oscore.final_score() == self.oscore.final_score_p2():
            return 'Tie'
        return 'player 2'   

    
    def run(self):
        while not self.game_over:
            self.handle_events()
            self.update()
            self.window.fill(BLACK)
            self.ogame.draw()
            self.oscore.draw_p1()
            self.oscore.draw_p2()
            self.otime.draw()
            
            pygame.display.update()
            self.clock.tick(30) 
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = GameManager()
    game.run()         
            





