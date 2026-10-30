
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
#txt font
SCOREFONT=pygame.font.SysFont("Comic Sans MS",40) #sets font styke/size


#passing width / height, and color.
class Spaceship(pygame.sprite.Sprite):
  def __init__(self,color,width,height,speed=1,health=5,points=0):
  #call parent class, Sprite, to access it
    pygame.sprite.Sprite.__init__(self)
    self.image=pygame.Surface([width,height]) 
    self.image.fill(color)
  #creates rectangle for the ships surface, Rect is saving position on the screen 
    pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
    self.rect=self.image.get_rect() 
  #additional attributes-
    self.speed=speed
    self.health=health
    self.points=points
  #Sets/Gets
  def set_speed(self,speed): 
    self.speed=speed 
  def set_color(self,color):
    self.color=color
  def set_health(self,health):
    self.health=health
  def get_health(self):
    return(self.health)
  
  def set_points(self,points):
    self.points=points
  def get_points(self):
    return(self.points)

  def decrease_health(self):
    """Decreases health variable, made for hit detect"""
    if self.health>=0:
      self.health-=1
    else:
      self.health=-1
    #print(self.get_health())

  def damage_indicator(self):
    """Recolors the ship based on damage (collision / enemy screen exit)"""
    global ship_color
    tupleconvert=list(ship_color)
    tupleconvert[0]+=51
    if tupleconvert[0]<=255:
      ship_color=tuple(tupleconvert)
    else:
      print("-1 Health State (dead)") #will lead to a gameover screen eventually

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
  def __init__(self,color,width,height,speedE=1,pointval=10):
    pygame.sprite.Sprite.__init__(self)
    self.image=pygame.Surface([width,height])
    self.image.fill(color)
    pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
    self.rect=self.image.get_rect()
    #spd
    self.speedE=speedE
    #point
    self.pointval=pointval
  def set_speed(self,speedE):
    self.speedE=speedE
  def set_pointval(self,pointval):
    self.pointval=pointval #new pointval

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
    enemy_=Enemy(APPLECOLOR,30,30,random.randint(1,7),1) #randomspeed / point default
    enemy_.rect.x=random.randint(120,650) #full screen x = 0-767
    enemy_.rect.y=5
    enemies_sprite.add(enemy_)
    #print(f"enemy {len(enemies_sprite)} made at X:{enemy_.rect.x}")
    #print(f"{len(enemies_sprite)} is moving at speed: {enemy_.speedE}")
    cooldown_ce=1

    if enemy_.speedE==1 or enemy_.speedE==2:
      print(f"Speed:{enemy_.speedE}, pts:{enemy_.pointval}")
    elif enemy_.speedE>2 and enemy_.speedE<6:
      enemy_.set_pointval(5)
      print(f"Speed:{enemy_.speedE}, pts:{enemy_.pointval}")
    elif enemy_.speedE==6 or enemy_.speedE==7:
      enemy_.set_pointval(10)
      print(f"Speed:{enemy_.speedE}, pts:{enemy_.pointval}")

def update_enemy():
  for enemy in enemies_sprite:
    enemy.rect.y+=1*enemy.speedE
    enemy.rect.x+=random.randint(-1,1) #Change these to two positives to watch it run away
    #print(f"enemy {len(enemies_sprite)} updated to X:{enemy.rect.x}")
    if enemy.rect.y>=999:
      enemies_sprite.remove(enemy)
      decrease_score()
      if ship_.points>0:
        update_scoretxt()
      elif ship_.points<0:
        #update_scoretxt()
        pass  #Lead to a gameover screen eventually
  enemies_sprite.update()
  enemies_sprite.draw(screen)

#colliding
def collision():
  """Check for intersection of rects (x/y) of all objects with eachother"""
  global ship_color
  #takes sprites in bullet & enemy groups, checks what to do if collided (kill or not), determines collision based on rect position
  enemy_hit=pygame.sprite.groupcollide(bullets_sprite,enemies_sprite,dokilla=True,dokillb=True,collided=pygame.sprite.collide_rect)
  player_hit=pygame.sprite.groupcollide(ships_sprite,enemies_sprite,False,True,pygame.sprite.collide_rect)

  if enemy_hit:
    print(f"Bullet hit, enemy #{len(enemies_sprite)} terminated")
    #score increase directly/link to score increase function (stage6) 
    increase_score()
    update_scoretxt()
    #print(f"Player has {ship_.get_points()} points")
    
  if player_hit:
    #changing ship color on hit
    ship_.damage_indicator()
    ship_.image.fill(ship_color)
    #changing health
    ship_.decrease_health()
    if ship_.health>=0:
      print(f"{ship_.health} hits remaining")
    else:
      print("Player has died (technically)")
    
def increase_score():
  """Increase player points based on certain condiions"""
  ship_.points+=10
  #print(f"Player has {ship_.get_points()} points")

def decrease_score():
  ship_.points-=10
  #print(f"-10 points, {ship_.get_points()} ")
  
def update_scoretxt():
  global scoretxt
  """Updating score txt and such"""
  scoretxt=SCOREFONT.render(f"Current Score: {ship_.points}",True,WHITE)
  

#make gameover function -needs to check decrease_health
  #def gameover yap

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
ship_=Spaceship(ship_color,P_WIDTH,P_HEIGHT,7,5) # <-- speed/health 
ship_.rect.x=500 
ship_.rect.y=800 
ships_sprite.add(ship_)

#Frame rate regulation 
clock = pygame.time.Clock() 

#text render guy
scoretxt=SCOREFONT.render(f"Current Score: {ship_.points}",True,WHITE) #Uses Font,
scoreRect=scoretxt.get_rect() #makes a rect for txt, allows to draw
#screen.blit(scoretxt,scoreRect)

#Game loop vari
keep_playing=True 
#Game Loop - updating/redrawing
while keep_playing: 
  #iterates over the current list of events(checks for events)  
  for event in pygame.event.get(): 
    keyinpt=pygame.key.get_pressed()
    if keyinpt[pygame.K_x]:
      event.type == pygame.QUIT
      keep_playing = False

  #screen drawing/display
  screen.fill((BLACK)) #recolors the screen 
  screen.blit(scoretxt,scoreRect)
  draw_player()
  
  #Game mechanic calls
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
