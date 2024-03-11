import pygame.font
from constants import *

class MessageManager:
    def __init__(self, window, font_size=36, font_color=(255, 255, 255)):
        self.window = window
        self.font_size = font_size
        self.font_color = font_color
        self.font = pygame.font.Font(None, self.font_size)
        self.messages = []

    
    def display_message(self, text, position):
        message = self.font.render(text, True, self.font_color)
        self.messages.append(message)
        self.window.blit(message, position)
        pygame.display.update() 

    
    def clear_messages(self):
        self.messages = []



#                             ---------------------test the code -------------------------
# if __name__ == '__main__':
#     import pygame
#     import sys

#     window_width = 900
#     window_height = 500
#     BLACK = (0, 0, 0)

#     pygame.init()
#     window = pygame.display.set_mode((window_width, window_height))
#     clock = pygame.time.Clock()
#     omessage = MessageManager(window)
    

#     while True:
#         for event in pygame.event.get():
#             if (event.type == pygame.QUIT):
#                 pygame.quit()
#                 sys.exit()

#         # Clear the screen
#         window.fill(BLACK)
#         omessage.display_message('Game Over - Time Expired', (window_width // 2, (window_height // 2)+ 100 ))
        
#         pygame.display.update()
#         clock.tick(30) 

