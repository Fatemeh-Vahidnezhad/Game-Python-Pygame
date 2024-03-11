import pygame 
from constants import * 
import cv2


class Fruit:

    def __init__(self, window, i, coin=False) -> None:
        self.window = window
        file_name = f"images/{i}.png"
        self.fruit_image = pygame.image.load(file_name)
        self.fruit_image = pygame.transform.scale(self.fruit_image, (cell_size[0] + 3, cell_size[1] + 3))

    # def Coin(self):
    #     return self.coin

    def get_rect(self, loc):
        rect = self.fruit_image.get_rect() 
        rect.topleft = loc
        return rect


    def get_size(self):
        return self.fruit_image.get_size()
    

    def grayscale(self):
        image_array = pygame.surfarray.array3d(self.fruit_image)
        return cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)


    def draw(self, loc):
        self.window.blit( self.fruit_image, loc)     

    # def draw_coin(self, loc):
    #     self.window.blit( self.coin, loc)     


     

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
#     ofruit1 = Fruit(window, 3)
#     ofruit2 = Fruit(window, 3)
#     fruit_surface2 = ofruit2.fruit_image
#     fruit_surface1 = ofruit1.fruit_image
#     ofruit1.are_images_equal(fruit_surface1, fruit_surface2)

#     while True:
#         for event in pygame.event.get():
#             if (event.type == pygame.QUIT):
#                 pygame.quit()
#                 sys.exit()

#     # Clear the screen
#         window.fill((255, 255, 255))

#         ofruit1.draw((100,200))
#         ofruit2.draw((400,200))
#         pygame.display.update()
#         clock.tick(30) 
