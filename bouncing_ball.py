import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600,600))
width = screen.get_width()
height = screen.get_height()

color = [
	(255, 0, 0),
	(255, 128, 0),
	(255, 255, 0),
	(0, 255, 0),
	(0, 0, 255)
]

#list of all balls
balls = []
ball_count = 50

#Ball constructer
class Ball:
	def __init__(self,radius, x, y, dx, dy, color):
		self.radius = radius
		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy
		self.color = color	
		
	def draw(self):
		pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
		pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), self.radius, 1)
		
	def update(self):
		
		if (self.x + self.radius) >= width or (self.x - self.radius) < 0:
			self.dx = -(self.dx)
	
		if (self.y + self.radius) >= height or (self.y - self.radius) < 0:
			self.dy = -(self.dy)
		
		self.x = self.x + self.dx
		self.y = self.y + self.dy	

for i in range(ball_count):
	x = random.random() * width
	y = random.random() * height
	dx = random.random()
	dy = random.random()
	radius = random.randint(30, 70)
	colorlength = len(color) - 1
	color_no = random.randint(0, colorlength)
	
	ball = Ball(radius, x, y, dx, dy, color[color_no])
	
        #inserting balls into an arry
	balls.append(ball)
	
def draw():
	for i in range(ball_count):
		balls[i].draw()
		balls[i].update()
				
def main():
	clock = pygame.time.Clock()
	
	while True:
		clock.tick()
		screen.fill((255, 255, 255))
		
		#events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
		
		#drawing all the balls
		draw()		
				
		pygame.display.flip()
		
if __name__ == "__main__":
	main()
		
