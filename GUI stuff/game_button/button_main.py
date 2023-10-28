import pygame as pg
import button
from os import path

img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')

#create display window
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption('Button Demo')

#load button images
start_img = pg.image.load(path.join(img_dir, "start.png")).convert_alpha()
exit_img = pg.image.load(path.join(img_dir, "exit.png")).convert_alpha()

#create button instances
start_button = button.Button(100, 200, start_img, 0.8)
exit_button = button.Button(450, 200, exit_img, 0.8)

#game loop
run = True
while run:

	screen.fill((202, 228, 241))

	if start_button.draw(screen):
		print('START')
	if exit_button.draw(screen):
		print('EXIT')

	#event handler
	for event in pg.event.get():
		#quit game
		if event.type == pg.QUIT:
			run = False

	pg.display.update()

pg.quit()