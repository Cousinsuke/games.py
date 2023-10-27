import pygame as pg
import random
from os import path
from settings_template import *

class Game:
    def __init__(self):
        #initialise game window
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        #start a new game
        self.all_sprites = pg.sprite.Group()
        g.run()

    def run(self):
        #game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        #game loop - update
        self.all_sprites.update()

    def events(self):
        #game loop - events
        for event in pg.event.get():
        # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        #game loop - draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        #game start screen
        pass

    def show_go_screen(self):
        #game over/continue screen
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()