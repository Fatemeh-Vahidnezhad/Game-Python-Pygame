from constants import *
# from board1 import * 
from Deck import * 
from fruit import *
# import time
# from player import *
# from score import *


class Game:
    def __init__(self, window) -> None:
        self.window = window
        self.oDeck = Deck(self.window)
        self.play_list = self.oDeck.playList()
        # self.oplayer = Player(self.window)
        # self.oscore = Score(self.window)


    def draw(self):
        for row in range(row_col_num[0]):
            for col in range(row_col_num[1]):
                # cnt += 1
                x = col * cell_size[0] + board_loc[0]
                y = row * cell_size[1] + board_loc[1]
                
                if self.play_list is not None:
                    index = row * row_col_num[1] + col
                    ofruit = self.play_list[index]  
                    ofruit.draw((x, y))


    def swap(self, index1, index2):
        print('swap--index1, index2', index1, index2)

        if self.oDeck.is_full() and index1 != index2:
            self.play_list[index1]  , self.play_list[index2] = self.play_list[index2], self.play_list[index1]
            self.draw()
            return index2
        else:
            return False
        
    def reset_board(self):
        self.oDeck.reset_board()


    def check_similar_in_a_row(self, index):   
        col = index % 4
        # if 2<= index <=13:
        self.ofruit1 = self.play_list[index]  

        
        if col == 0:
            print('col==0')
            ofruit3 = self.play_list[index + 2] 
            ofruit2 = self.play_list[index + 1] 
            # 0, 1, 2
            similarity1 = self.oDeck.compare_images(self.ofruit1.grayscale(), ofruit2.grayscale())
            similarity2 = self.oDeck.compare_images(ofruit2.grayscale(), ofruit3.grayscale())

            if (similarity1 ==True and similarity2 == True):
                return True
            
        elif col == 3:
            print('col==3')
            ofruit_1 = self.play_list[index - 2]
            ofruit0 = self.play_list[index - 1]
            # -2, -1, 0
            similarity3 = self.oDeck.compare_images(self.ofruit1.grayscale(), ofruit0.grayscale())
            similarity4 = self.oDeck.compare_images(ofruit0.grayscale(), ofruit_1.grayscale())

            if (similarity3 ==True and similarity4 == True):
                return True
        
        elif col == 2:
            print('col==2')
            ofruit0 = self.play_list[index - 1]
            ofruit2 = self.play_list[index + 1] 
            ofruit_1 = self.play_list[index - 2]

            # -1, 0, 1
            similarity5 = self.oDeck.compare_images(self.ofruit1.grayscale(), ofruit0.grayscale())
            similarity6 = self.oDeck.compare_images(self.ofruit1.grayscale(),ofruit2.grayscale())
            # -2, -1, 0
            similarity3 = self.oDeck.compare_images(self.ofruit1.grayscale(), ofruit0.grayscale())
            similarity4 = self.oDeck.compare_images(ofruit0.grayscale(), ofruit_1.grayscale())

            if (similarity5 ==True and similarity6 == True) or (similarity3 ==True and similarity4 == True):
                return True 
            
        else:
            print('col==1')
            ofruit0 = self.play_list[index - 1]
            ofruit2 = self.play_list[index + 1] 
            ofruit3 = self.play_list[index + 2] 

            # -1, 0, 1
            similarity5 = self.oDeck.compare_images(self.ofruit1.grayscale(), ofruit0.grayscale())
            similarity6 = self.oDeck.compare_images(self.ofruit1.grayscale(),ofruit2.grayscale())
            
             # 0, 1, 2
            similarity1 = self.oDeck.compare_images(self.ofruit1.grayscale(), ofruit2.grayscale())
            similarity2 = self.oDeck.compare_images(ofruit2.grayscale(), ofruit3.grayscale())

            if (similarity5 ==True and similarity6 == True) or (similarity1 ==True and similarity2 == True):
                return True 
            
