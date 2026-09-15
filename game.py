
import pygame

#Not sure what this does outside of codio, anchored the screen?
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)

#start the pygame module 
pygame.init() 

#window size: 
screen_width=1000
screen_height=1000

#variable initializers 
#testing varis, change later
COLOR=(0,0,255)
PURPLE=(230,255,250)
WIDTH=500
HEIGHT=400

#passing width / height, and color. (May or may not need the color later?)
class Spaceship(pygame.sprite.Sprite):
  def __init__(self,color,width,height):
    #call parent class, Sprite, to access it
    pygame.sprite.Sprite.__init__(self)
    self.image=pygame.Surface([width,height]) #gonna need to make a width/height variable
    self.image.fill(color) #change this to spaceship img instead later
    
    #creates rectangle for the ships surface-Rect is saving position on the screen 
    pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
    self.rect=self.image.get_rect() 

#screen & dimensions 
screen = pygame.display.set_mode((screen_width, screen_height)) 

#Window Name / Color
pygame.display.set_caption("Game Window")  
screen.fill((0, 0, 100))

#Making the objects 
sprites_list=pygame.sprite.Group() #holds sprites in a list to pull from later
#idk if object_ is just a variable name or required, ill mess with it more if this works
#Making the OBJ (ship) and deciding its position on screen (rect.x/y)
object_=Spaceship(PURPLE,50,60)
object_.rect.x=100
object_.rect.y=200
sprites_list.add(object_) #adds to the big beautiful sprite list!! (only thing in there lol)

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
  sprites_list.update()
  sprites_list.draw(screen)
  pygame.display.flip() #this updates the WHOLE screen. idk why its named flip <_< 
   

  #Updates & Framerate 
  #pygame.display.update() commenting this out while I have the flipster 
  clock.tick(60) 

#quits the pygame module 
pygame.quit() 
quit() 
