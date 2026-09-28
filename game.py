
import pygame

#Not sure what this does outside of codio, anchored the screen?
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)

#start the pygame module 
pygame.init() 

#window size: 
screen_width=800
screen_height=900

#variable initializers / constants 
#testing varis, change later
COLOR=(0,0,255)
PURPLE=(127,0,255)
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

def movement():
    """Check if/what movemnt key is pressed, then calculate new pos."""
    keyinp=pygame.key.get_pressed() #access the keyname stuff yeah ea 

    if keyinp[pygame.K_LEFT]:
      object_.rect.x-=1 
    elif keyinp[pygame.K_RIGHT]:
      object_.rect.x+=1 

    """elif keyinp[pygame.K_UP]:
      object_.rect.y-=1 
    elif keyinp[pygame.K_DOWN]:
      object_.rect.y+=1"""

def drawing():
  """Visual parts of the game"""
  #all items drawn to the screen are handled here. (GRABS EVERY SPRITE IN THIS LIST)
  sprites_list.update() 
  sprites_list.draw(screen) #draws all sprites (in sprite list) onto the screen surface

#screen & dimensions 
screen = pygame.display.set_mode((screen_width, screen_height)) 

#Window Name / Color
pygame.display.set_caption("Game Window")  
screen.fill((255, 255, 255))

#Making the objects 
sprites_list=pygame.sprite.Group() #holds sprites in a list to pull from later

#Making the OBJ (ship) and deciding its position on screen (rect.x/y)
object_=Spaceship(PURPLE,70,60)
object_.rect.x=500 #idk if object_ is just a variable name or required, ill mess with it more if this works
object_.rect.y=800 
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
  
  #screen drawing
  screen.fill((255,255,255)) #recolors the screen 
  drawing() #this draws EVERYTHING instead of js the player, maybe change that later?
    
  #Updates & Framerate 
  movement() 
  pygame.display.update()
  clock.tick(100) 

#quits the pygame module 
pygame.quit() 
quit() 
