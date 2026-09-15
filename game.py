
import pygame

#Not sure what this does outside of codio, anchored the screen?
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)

#start the pygame module 
pygame.init() 

#window size: 
screen_width=1000
screen_height=700 

#variable initializers 
#testing varis, change later
COLOR=(230,230,250)
WIDTH=(1)
HEIGHT=(2)

#passing width / height, and color. (May or may not need the color later?)
class Spaceship(pygame.sprite.Sprite):
  def __init__(self,color,width,height):
    #call parent class, Sprite, to access it
    pygame.sprite.Sprite.__init__(self)
    self.image=pygame.Surface([width,height]) #gonna need to make a width/height variable
    self.image.fill(color) #change this to spaceship img instead later
    #creates rectangle for the ships surface
    self.rect=self.image.get_rect() 

#screen & dimensions 
screen = pygame.display.set_mode((screen_width, screen_height)) 

#Window Name / Color
pygame.display.set_caption("Game Window")  
screen.fill((0, 100, 250))


#Frame rate regulation 
clock = pygame.time.Clock() 

#Game loop vari
keep_playing=True 
#Game Loop - updating/redrawing
while keep_playing: 

  #iterates over the current list of events(checks for events)  
  for event in pygame.event.get(): 
    #If ESC, quit
    if event.type == pygame.QUIT: 
      keep_playing = False
  
  

  #all items drawn to the screen go here
  # > Draw up spaceship onto screen

  #Updates & Framerate 
  pygame.display.update() 
  clock.tick(60) 

#quits the pygame module 
pygame.quit() 
quit() 
