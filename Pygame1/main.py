import pygame
import sys
from Character.sprite import *
from Xuly.background import *

if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

pygame.init()
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
img = pygame.image.load('image/hulk2.png')
FRAME_WIDTH = 180
FRAME_HEIGHT = 260

setBackgroundImage('image/background_Play.png')

hulk=Sprite(0,0)

nextFrame = 0
frame=0
time_clock = 0
frame_last_x=0
frame_last_y=0
def draw(hulk):
	global frame
	global nextFrame
	global time_clock
	global frame_last_y
	time_clock+=1
	if time_clock>nextFrame:
		frame=(frame+1)%4
		nextFrame+=5
	if keyPressed("right"):
		scrollBackground(-10,0)
		screen.blit(img, (hulk.getX(), hulk.getY()), (frame*45, 130, hulk.getW(), hulk.getH()))
		frame_last_y=130
	elif keyPressed("up"):
		scrollBackground(0,10)
		screen.blit(img, (hulk.getX(), hulk.getY()), (frame*45, 195, hulk.getW(), hulk.getH()))
		frame_last_y=195
	elif keyPressed("down"):
		scrollBackground(0,-10)
		screen.blit(img, (hulk.getX(), hulk.getY()), (frame*45, 0, hulk.getW(), hulk.getH()))
		frame_last_y=0
	elif keyPressed("left"):
		scrollBackground(10,0)
		screen.blit(img, (hulk.getX(), hulk.getY()), (frame*45, 65, hulk.getW(), hulk.getH()))
		frame_last_y=65
	else:
		scrollBackground(0,0)
		screen.blit(img, (hulk.getX(), hulk.getY()), (frame_last_x, frame_last_y, hulk.getW(), hulk.getH()))


while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        handle(event,hulk)

    hulk.move()
    #screen.fill((95, 183, 229)) # sky color
    if pygame.font:
        font = pygame.font.Font(None, 36)
        #text = font.render("Hello World !", 1, (255, 0, 0))
        #textpos = text.get_rect(centerx=width/2)
        #screen.blit(text, textpos)
    time_clock+=1
    draw(hulk)  
    pygame.display.flip()








