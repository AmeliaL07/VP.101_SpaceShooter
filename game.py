
import pygame
import random 
#Not sure what this does outside of codio, anchored the screen?
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)

#start the pygame module 
pygame.init() 

#window size: 
screen_width=800
screen_height=900

#variable initializers
#colors
WHITE=(255,255,255)
BLACK=(0,0,0)
APPLECOLOR=(66,200,99)
ship_color=(0, 221, 255) #og is 127,0,255
#width/height
P_WIDTH=30
P_HEIGHT=60
#cooldowns
cooldown_cb=0
cooldown_ce=0

#passing width / height, and color.
class Spaceship(pygame.sprite.Sprite):
  def __init__(self,color,width,height,speed=1):
    #call parent class, Sprite, to access it
    pygame.sprite.Sprite.__init__(self)
    self.image=pygame.Surface([width,height]) 
    self.image.fill(color)
    #creates rectangle for the ships surface, Rect is saving position on the screen 
    pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
    self.rect=self.image.get_rect() 
    #speed attri -
    self.speed=speed
  def set_speed(self,speed): #allows speed to be changed
    self.speed=speed 
    #color get-set
  def set_color(self,color):
    self.color=color
    #bane of my existence VVV
  def hit_recolor(self):
    global ship_color
    tupleconvert=list(ship_color)
    tupleconvert[0]+=51
    ship_color=tuple(tupleconvert)

class Bullet(pygame.sprite.Sprite):
  def __init__(self,color,width,height,speedB=1):
    pygame.sprite.Sprite.__init__(self)
    self.image=pygame.Surface([width,height]) #w/h of bullet
    self.image.fill(color) #clr of bullet
    pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height)) 
    self.rect=self.image.get_rect()
    #speed
    self.speedB=speedB
  def set_speed(self,speedB):
    self.speedB=speedB 

class Enemy(pygame.sprite.Sprite):
  def __init__(self,color,width,height,speedE=1):
    pygame.sprite.Sprite.__init__(self)
    self.image=pygame.Surface([width,height])
    self.image.fill(color)
    pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
    self.rect=self.image.get_rect()
    #spd
    self.speedE=speedE
  def set_speed(self,speedE):
    self.speedE=speedE

#PLAYER FUNCTIONS
def movement():
    """Check if/what movemnt key is pressed, then calculate new pos."""
    keyinpt=pygame.key.get_pressed() #access the keyname stuff yeah ea 
    if keyinpt[pygame.K_LEFT]:
      ship_.rect.x-=1*ship_.speed 
      #print(f"Player X:{ship_.rect.x}") 
    elif keyinpt[pygame.K_RIGHT]:
      ship_.rect.x+=1*ship_.speed 
      #print(f"Player X:{ship_.rect.x}")
    
def draw_player():
  """Visual of player spaceship"""
  ships_sprite.update() 
  ships_sprite.draw(screen) 

#BULLET FUNCTIONS
def create_bullet():
  """Create a bullet object, default spawn above player."""
  bullet_=Bullet(WHITE,16,8,8)
  bullet_.rect.x=ship_.rect.x #puts bullet at current player position
  bullet_.rect.y=ship_.rect.y-5
  bullets_sprite.add(bullet_)
  #print(f"bullet # made: {len(bullets_sprite)}")

def cooldown_b():
  """increases cooldown/resets"""
  global cooldown_cb
  if cooldown_cb>=30: #if hit cooldown
    cooldown_cb=0 #reset it
    #print("I DONT")
  elif cooldown_cb>0: 
    cooldown_cb+=1 
    #print("I GO UP")

def fire_bullet():
  cooldown_b()
  global cooldown_cb
  keyinpt=pygame.key.get_pressed()
  if keyinpt[pygame.K_SPACE] and cooldown_cb==0:
    create_bullet()
    cooldown_cb=1

def update_bullet():
  """Draws the bullet/updates Y position upward"""
  for bullet in bullets_sprite:
    bullet.rect.y-=1*bullet.speedB
    if(bullet.rect.y<=0):
      bullets_sprite.remove(bullet) 
      #print(f"Bullet removed")
  bullets_sprite.update()
  bullets_sprite.draw(screen)

#ENEMIES
def cooldown_e():
  """increases cooldown/resets"""
  global cooldown_ce
  if cooldown_ce>=70: #if hit cooldown
    cooldown_ce=0 #reset it
    #print("I DONT")
  elif cooldown_ce>0: 
    cooldown_ce+=1 
    #print("I GO UP")

def create_enemy():
  """Create enemy object (eek!)"""
  cooldown_e()
  global cooldown_ce
  if cooldown_ce==0:
    enemy_=Enemy(APPLECOLOR,30,30,random.randint(3,7)) #experimenting w/random speeds
    enemy_.rect.x=random.randint(120,650) #full screen x = 0-767
    enemy_.rect.y=5
    enemies_sprite.add(enemy_)
    #print(f"enemy {len(enemies_sprite)} made at X:{enemy_.rect.x}")
    #print(f"{len(enemies_sprite)} is moving at speed: {enemy_.speedE}")
    cooldown_ce=1

def update_enemy():
  for enemy in enemies_sprite:
    enemy.rect.y+=1*enemy.speedE
    enemy.rect.x+=random.randint(-1,1) #Change these to two positives to watch it run away
    #print(f"enemy {len(enemies_sprite)} updated to X:{enemy.rect.x}")
  enemies_sprite.update()
  enemies_sprite.draw(screen)

#colliding
def collision():
  """Checks if a bullets rect collides with an Enemies rect, will terminate both if true"""
  """ALSO compares rect of player and enemy, supposed to term enemy and alter spaceships color if collision is true"""
  global ship_color
  #takes sprites in bullet & enemy groups, checks what to do if collided (kill or not), determines collision based on rect position
  enemy_hit=pygame.sprite.groupcollide(bullets_sprite,enemies_sprite,dokilla=True,dokillb=True,collided=pygame.sprite.collide_rect)
  player_hit=pygame.sprite.groupcollide(ships_sprite,enemies_sprite,False,True,pygame.sprite.collide_rect)
  if enemy_hit:
    print(f"Bullet hit, enemy #{len(enemies_sprite)} terminated")
    #score increase directly/link to score increase function (stage6)
  if player_hit:
    print("oww")
    #changing ship color on hit
    ship_.hit_recolor()
    ship_.image.fill(ship_color)
  
#screen & dimensions 
screen = pygame.display.set_mode((screen_width, screen_height)) 
#Window Name / Color
pygame.display.set_caption("Game Window")  
screen.fill(BLACK)

#Objects lists 
ships_sprite=pygame.sprite.Group() #ship group -rlly pointless cause theres only 1 ship.
bullets_sprite=pygame.sprite.Group() #bullets group/list
enemies_sprite=pygame.sprite.Group() #enemies group/list

#Making OBJ (ship)+ starting position(rect.x/y)
ship_=Spaceship(ship_color,P_WIDTH,P_HEIGHT,7) # <-- speed 
ship_.rect.x=500 
ship_.rect.y=800 
ships_sprite.add(ship_)

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
  screen.fill((BLACK)) #recolors the screen 
  draw_player()
  movement()
  fire_bullet()
  create_enemy()
  collision()

  #Updates & Framerate 
  update_bullet()
  update_enemy()
  pygame.display.update()
  clock.tick(60) 

#quits the pygame module 
pygame.quit() 
quit() 
