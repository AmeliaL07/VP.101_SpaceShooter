#randum code to test if pygame works

import pygame

class Ball:
  def __init__(self, surface, color, x, y, r):
    self.surface = surface
    self.color = color
    self.x = x
    self.y = y
    self.r = r
    self.vel_x = 1
    self.vel_y = 2
    
  def draw(self):
    pygame.draw.circle(self.surface, self.color, (self.x, self.y), self.r)
    
  def update(self):
    self.move()
    self.bounce()
    
  def move(self):
    self.x += self.vel_x
    self.y += self.vel_y
    
  def bounce(self):
    if self.x < self.r or self.x > 400 - self.r:
      self.vel_x *= -1
    if self.y < self.r or self.y > 400 - self.r:
      self.vel_y *= -1
    
pygame.init()
window = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Bouncing Ball")
clock = pygame.time.Clock()
ball = Ball(window, (255, 0, 0), 20, 20, 20)
run = True
while run:
  window.fill((120, 120, 120))
  ball.draw()
  ball.update()
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  pygame.display.update()
  clock.tick(30)
pygame.quit()

x=input("Enter test data: ")
print("Test")
print(x)