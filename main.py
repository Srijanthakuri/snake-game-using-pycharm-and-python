import pygame
from pygame.locals import*
import time

size=40

class apple():
    def __init__(self,parent_screen):
        self.parent_screen=parent_screen
        self.image=pygame.image.load("Resources/apple.jpg")
        self.x=size*3
        self.y=size*3
    def draw(self):
        self.parent_screen.blit(self.image,(self.x,self.y))
        pygame.display.flip()
    

class snake():
    def __init__(self,parent_screen,length):
        self.length=length
        self.parent_screen=parent_screen
        self.block=pygame.image.load("Resources/block.jpg").convert()
        self.x=[size]*length
        self.y=[size]*length
        self.direction='down'

    def draw(self):
        self.parent_screen.fill((255,255,255))
        for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i],self.y[i]))
        pygame.display.flip()
    
    def move_up(self):
        self.direction='up'
    def move_down(self):
        self.direction='down'
    def move_left(self):
        self.direction='left'
    def move_right(self):
        self.direction='right'
        
    def move(self):
        for i in range(self.length-1,0,-1):
            self.x[i]=self.x[i-1]
            self.y[i]=self.y[i-1]
        if self.direction=='up':
            self.y[0]-=size
        if self.direction=='down':
            self.y[0]+=size
        if self.direction=='left':
            self.x[0]-=size
        if self.direction=='right':
            self.x[0]+=size
        self.draw()
    
class game():
    def __init__(self):
        pygame.init()
        self.surface=pygame.display.set_mode((800,800))
        self.surface.fill((255,255,255))
        self.snake=snake(self.surface,6)
        self.snake.draw()
        self.apple=apple(self.surface)
        self.apple.draw()
    
    def play(self):
        self.snake.move()
        self.apple.draw()
    
    def run(self):
        running=True
    
        while running:
            for event in pygame.event.get():
                if  event.type==KEYDOWN:
                    if event.key==K_ESCAPE:
                        running=False
                    if event.key==K_UP:
                        self.snake.move_up()
                    if event.key==K_DOWN:
                        self.snake.move_down()
                    if event.key==K_LEFT:
                        self.snake.move_left()
                    if event.key==K_RIGHT:
                        self.snake.move_right()
                elif event.type==QUIT:
                    running=False
            self.play()
            time.sleep(0.5)    
    


    
if __name__=="__main__":
    game=game()
    game.run()
    
    
   
    