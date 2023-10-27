import pygame as pg
import random
import os

WIDTH = 800
HEIGHT = 700
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# setup assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

class Player(pg.sprite.Sprite):
    #sprite for the player
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.rotozoom(pg.image.load(os.path.join(img_folder, "swaggersouls.png")).convert(),0,0.2)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.y_speed = 5

    def update(self):
        self.rect.x += 5
        self.rect.y += self.y_speed
        if self.rect.bottom > HEIGHT - 200:
            self.y_speed = -5
        if self.rect.top < 300:
            self.y_speed = 5
        if self.rect.left > WIDTH:
            self.rect.right = 0

# initialize pygame and create window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game")
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
player = Player()
all_sprites.add(player)
# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pg.event.get():
        # check for closing window
        if event.type == pg.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(BLUE)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pg.display.flip()

pg.quit()