import pygame
import random
import time
from PIL import Image
# new import 
import pygame.surfarray as surfarray
import sys 
import random
from pygame.locals import *
from itertools import cycle

pygame.init()

display_width = 800
display_height = 600
#display_width = 288
#display_height = 512

game_window_size = (display_width, display_height)

# Color definitions
white = (255, 255, 255)
black = (0, 0, 0)

SCREEN = pygame.display.set_mode(game_window_size)
pygame.display.set_caption('test')
clock = pygame.time.Clock()

car_img = pygame.image.load('pygame_car_race-master/Car.png')
im = Image.open('pygame_car_race-master/Car.png')
car_width, car_height = im.size

class Game:
    def __init__(self):
        self.score = 0
        self.playerx = display_width * 0.45
        self.playery = display_height * 0.8
        self.playerx_displacement = 0
        self.PLAYER_LEFT_MOVE = 0
        self.PLAYER_RIGHT_MOVE = 1
        self.VALID_ACTIONS = 2
        self.actions = list([0, 0])

        self.FPS = 30
        self.obstacle_startx = random.randrange(0, display_width)
        self.obstacle_starty = -600
        self.obstacle_speed = 10
        self.obstacle_width = 100
        self.obstacle_height = 100
        #self._is_crash = False      # set is crash to false to restart
    
    def draw_car(self, x ,y):
        # blit prepare the image to display in background and show once update
        # is called
        SCREEN.blit(car_img, (x,y))

    def show_crash_msg(self):
        def text_objects(text, font):
            ts = font.render(text, True, black)
            return ts, ts.get_rect()
        
        text = 'Crashed!!!'
        large_text = pygame.font.Font('freesansbold.ttf', 115)
        text_surface, text_rect = text_objects(text, large_text)
        text_rect.center = (display_width/2, display_height/2)
        SCREEN.blit(text_surface, text_rect)

        pygame.display.update()
        time.sleep(0.5)
        #self.game_loop()
        self.__init__()
        temp = [1,0,0]
        self.frame(temp)

    def things_dodged(self, count):
        font = pygame.font.SysFont(None, 25)
        text = font.render("Dodged: "+str(count), True, black)
        SCREEN.blit(text,(0,0))

    def draw_things(self, thingx, thingy, thingw, thingh, color):
        pygame.draw.rect(SCREEN, color, [thingx, thingy, thingw, thingh])

    def _is_crash(self):
        if self.playerx  > display_width - car_width or self.playerx  < 0:
            return True

        if self.playery < self.obstacle_starty+self.obstacle_height:
            if self.playerx  > self.obstacle_startx and self.playerx  < self.obstacle_startx + self.obstacle_width or self.playerx + car_width > self.obstacle_startx and self.playerx + car_width < self.obstacle_startx+self.obstacle_width:
                return True

        return False
    #def frame(self, input_actions):
    def frame(self, deep_action):
        terminal = False
        if deep_action[0] != 1:
            if deep_action[1] == 1:
                self.actions[self.PLAYER_LEFT_MOVE] = 1
                self.actions[self.PLAYER_RIGHT_MOVE]=0
                self.playerx_displacement = -5
            elif deep_action[2] == 1:
                self.actions[self.PLAYER_LEFT_MOVE] = 0
                self.actions[self.PLAYER_RIGHT_MOVE] = 1
                self.playerx_displacement = 5
        if deep_action[0] == 1:
            self.actions[self.PLAYER_LEFT_MOVE] = 0
            self.actions[self.PLAYER_RIGHT_MOVE] = 0
            self.playerx_displacement = 0  
#        self.frame(1)
#        pygame.quit()
#        quit()

        self.playerx += self.playerx_displacement
        #terminal = False
        SCREEN.fill(white)

        self.draw_things(self.obstacle_startx, self.obstacle_starty, self.obstacle_width, self.obstacle_height, black)
        self.draw_car(self.playerx,self.playery)
        self.things_dodged(self.score)
        self.obstacle_starty += self.obstacle_speed
        """
        Ning-Hsu 2020/01/28
        added reward for training
        """
        reward = 0.1

        if self.obstacle_starty > display_height:
            self.obstacle_starty = 0 - self.obstacle_height
            self.obstacle_startx = random.randrange(0,display_width)
            self.score += 1
            # to increase obstacle speed
            self.obstacle_speed += 0.5
            # to increase the width of obstacle
            # self.obstacle_width += (self.score * 1.2)
            """
            Ning-Hsu 2020/01/28
            added reward for passing obstacles
            """
            reward = 1
        
        if self._is_crash():
            terminal = True
            self.show_crash_msg()
            self.__init__()
            #terminal = True
            self.score = 0
            """
            Ning-Hsu 2020/01/28
            added neg reward as penalty for crashing
            """
            reward = -10
        pygame.display.update()
        clock.tick(self.FPS) # Frames per second

        image_data = pygame.surfarray.array3d(pygame.display.get_surface())
        # return image_data, self.score, terminal
        """
        Ning-Hsu 2020/01/28
        return reward instead of entire score
        """
        return image_data, reward, terminal


#g = Game()
#g.game_loop()

