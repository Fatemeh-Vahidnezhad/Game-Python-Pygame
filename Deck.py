from fruit import * 
import random
from constants import *
import imagehash
from PIL import Image
import cv2
from skimage.metrics import structural_similarity as ssim



class Deck:
    def __init__(self, window) -> None:
        self.window = window
        self.start_list = []
        # self.play_list = []
        self.create_fruit()


    def reset_board(self):
        self.create_fruit()

    def create_fruit(self):
        for i in range(1, 17):
            num = random.randint(1,9)
            ofruit = Fruit(self.window, num)
            self.start_list.append(ofruit)

    def is_full(self):
        return all(fruit is not None for fruit in self.start_list)


    def compare_images(self, img1, img2):

        similarity_index, _ = ssim(img1, img2, full = True)
        threshold = 0.8
        if similarity_index >= threshold:
            # print("Images are similar.")
            return True
        # else:
            # print("Images are not similar.")  
            # return False


    def playList(self):
        return self.start_list

    def get_fruit(self):
        while not self.is_empty():
            return self.start_list.pop()
    
    def is_empty(self):
        if  self.len_list() == 0:
            return True
        else:
            return False

    def len_list(self): 
        # if len(self.play_list) == 0:
        #     raise IndexError('no more fruits')
        # else:
        return len(self.start_list)

               

                            # ---------------------test the code -------------------------
# if __name__ == '__main__':
#     import pygame
#     import sys

#     window_width = 1000
#     window_height = 800
#     BLACK = (0, 0, 0)

#     pygame.init()
#     window = pygame.display.set_mode((window_width, window_height))
#     clock = pygame.time.Clock()
#     oDeck = Deck(window)

#     # print(oDeck.play_list)
#     while True:
#         for event in pygame.event.get():
#             if (event.type == pygame.QUIT):
#                 pygame.quit()
#                 sys.exit()

#         # Clear the screen
#         window.fill(BLACK)
#         oDeck.draw()
#         pygame.display.update()
#         pygame.display.flip()
#         clock.tick(30) 

