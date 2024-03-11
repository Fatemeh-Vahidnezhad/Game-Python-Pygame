import pyghelpers
from  constants import *
import pygwidgets


class Time:
    def __init__(self, window ) -> None:
        self.window = window
        self.seconds = initial_time
        self.oCountDownTimer = pyghelpers.CountDownTimer(self.seconds)  # create a count down clock timer
        self.start_timer()
       
    def start_timer(self):
        self.oCountDownTimer.start()  # start the clock running
    
    def reset_timer(self):
        self.seconds = initial_time
        self.oCountDownTimer.reset()


    def get_count_down(self):
        return self.oCountDownTimer
    
    def is_expired(self):
        return self.oCountDownTimer.getTime() <= 0


    # def update(self):
    #     pass

    def draw(self):
        time_to_show = self.oCountDownTimer.getTimeInHHMMSS(1)
        self.timer_display = pygwidgets.DisplayText(self.window, (20, 485), '', fontSize=36, textColor=WHITE)
        self.timer_display.setValue('Time: ' + time_to_show)
        self.timer_display.draw()
    
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
#     otime = Time(window)
#     while True:
#         for event in pygame.event.get():
#             if (event.type == pygame.QUIT):
#                 pygame.quit()
#                 sys.exit()

#         # Clear the screen
#         window.fill(BLACK)
#         otime.draw()
        
#         pygame.display.update()
#         clock.tick(30) 