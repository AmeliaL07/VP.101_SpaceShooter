
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
WHITE=(255,255,255)
BLACK=(0,0,0)
PURPLE=(127,0,255)
P_WIDTH=30
P_HEIGHT=60


#passing width / height, and color. (color comes in w/obj call)
class Spaceship(pygame.sprite.Sprite):
  def __init__(self,color,width,height):
    #call parent class, Sprite, to access it
    pygame.sprite.Sprite.__init__(self)
    self.image=pygame.Surface([width,height]) #gonna need to make a width/height variable
    self.image.fill(color) #change this to spaceship img instead later
    
    #creates rectangle for the ships surface, Rect is saving position on the screen 
    pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
    self.rect=self.image.get_rect() 

class Bullet(pygame.sprite.Sprite):
  def __init__(self,color,width,height):
    pygame.sprite.Sprite.__init__(self)
    self.image=pygame.Surface([width,height]) #w/h of bullet
    self.image.fill(color) #clr of bullet

    #kinda unsure about these & what they actually DO? VV
    pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height)) 
    self.rect=self.image.get_rect()

def movement():
    """Check if/what movemnt key is pressed, then calculate new pos."""
    keyinpt=pygame.key.get_pressed() #access the keyname stuff yeah ea 

    if keyinpt[pygame.K_LEFT]:
      object_.rect.x-=1 
    elif keyinpt[pygame.K_RIGHT]:
      object_.rect.x+=1 

    """elif keyinp[pygame.K_UP]:
      object_.rect.y-=1 
    elif keyinp[pygame.K_DOWN]:
      object_.rect.y+=1"""

def draw_player():
  """Visual parts of the game"""
  #all items drawn to the screen are handled here. (GRABS EVERY SPRITE IN THIS LIST)
  ships_sprite.update() 
  ships_sprite.draw(screen) #draws all sprites (in sprite list) onto the screen surface

def create_bullet():
  """Create a bullet object, default spawn above player."""
  keyinpt=pygame.key.get_pressed()
  if keyinpt[pygame.K_SPACE]:
    bullet_=Bullet(BLACK,10,10)
    bullet_.rect.x=object_.rect.x
    bullet_.rect.y=750
    bullets_sprite.add(bullet_) #add to group
    #checking for bullet creation
    print(f"bullet made {len(bullets_sprite)}") 
    
def update_bullet():
  """Draws the bullet/updates X/Y position"""
  #Change X position of the bullet relative to the player
  for bullet in bullets_sprite:
    bullet.rect.y-=1
  #Maybe just have Y 
  bullets_sprite.update()
  bullets_sprite.draw(screen)

#screen & dimensions 
screen = pygame.display.set_mode((screen_width, screen_height)) 

#Window Name / Color
pygame.display.set_caption("Game Window")  
screen.fill(WHITE)

#Making the objects 
ships_sprite=pygame.sprite.Group() #ship group -rlly pointless cause theres only 1 ship.
bullets_sprite=pygame.sprite.Group() #bullets group/list 

#Making the OBJ (ship) and deciding its position on screen (rect.x/y)
object_=Spaceship(PURPLE,P_WIDTH,P_HEIGHT)
object_.rect.x=500 
object_.rect.y=800 
ships_sprite.add(object_) #adds spaceship into ships_sprite 

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
  
  draw_player()
  create_bullet()

  #Updates & Framerate 
  movement()
  update_bullet()
  pygame.display.update()
  clock.tick(100) 

#quits the pygame module 
pygame.quit() 
quit() 
