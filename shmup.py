import pygame as pg
import random
from os import path

img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')

#game options/settings
TITLE = "Shmup 911 game"
WIDTH = 480
HEIGHT = 600
FPS = 60
POWERUP_TIME = 5000

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# initialize pygame and create window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(TITLE)
clock = pg.time.Clock()

font_name = pg.font.match_font('arial')
def draw_text(surf , text, size, x, y ):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text , True , WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit (text_surface, text_rect)

def newmob():
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

#draw shield to screen
def draw_shield_bar(surf, x, y, pct):
    if pct <0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (pct / 3) * BAR_LENGTH
    outline_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pg.Rect(x, y, fill, BAR_HEIGHT)
    pg.draw.rect(surf, GREEN, fill_rect)
    pg.draw.rect(surf, WHITE, outline_rect, 2)

# draw lives to screen
def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 33 * i
        img_rect.y = y
        surf.blit(img, img_rect)

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(player_img, (75, 75))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.radius = (20)
        # pg.draw.circle(self.image , RED, self.rect.center, self.radius)
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.shield = 3
        self.shoot_delay = 250
        self.last_shot = pg.time.get_ticks()
        self.lives = 3
        self.hidden = False 
        self.hide_timer = pg.time.get_ticks()
        self.power = 1
        self.power_time = pg.time.get_ticks()
 
    def update(self):
        #timeout for powerups
        if self.power >= 2 and pg.time.get_ticks() - self.power_time > POWERUP_TIME:
            self.power -= 1
            self.power_time = pg.time.get_ticks()

        #unhide if hidden
        if self.hidden and pg.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.centerx = WIDTH / 2
            self.rect.bottom =  HEIGHT - 10

        self.speedx = 0
        self.speedy = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT]:
            self.speedx = -5
        if keystate[pg.K_RIGHT]:
            self.speedx = 5
        if keystate[pg.K_SPACE]:
            self.shoot()
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def powerup(self):
        self.power += 1
        self.power_time = pg.time.get_ticks()

    def shoot (self):
        now = pg.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            if self.power == 1:
                bullet = Bullet(self.rect.centerx, self.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
                shoot_sound.play()
            if self.power >= 2:
                bullet1 = Bullet(self.rect.left, self.rect.centery)
                bullet2 = Bullet(self.rect.right, self.rect.centery)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet1)
                bullets.add(bullet2)
                shoot_sound.play()

    def hide(self): # hide the player temporarly
        self.hidden = True
        self.hide_timer = pg.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT + 200)


class Mob(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image_orig = pg.transform.scale(random.choice(towers_images), (50, 75))
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3) 
        # rotate mob
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pg.time.get_ticks()

    def rotate(self):
        now = pg.time.get_ticks()
        if  now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pg.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center 
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center
        
    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)


class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves of the top of the screen
        if self.rect.bottom < 0:
            self.kill()

class Pow(pg.sprite.Sprite):
    def __init__(self, center):
        pg.sprite.Sprite.__init__(self)
        self.type = random.choice(['shield', 'gun'])
        self.image = powerup_images[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 4

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves of the top of the screen
        if self.rect.top > HEIGHT:
            self.kill()

class Explosion(pg.sprite.Sprite):
    def __init__(self, center, size):
        pg.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pg.time.get_ticks()
        self.frame_rate = 75

    def update(self):
        now = pg.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
    
    #gameover screen
def show_go_screen():
    screen.blit(background, background_rect)
    draw_text(screen, "911 Game", 64, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "Arrow keys move, Space to fire", 22, WIDTH / 2, HEIGHT / 2)
    draw_text(screen, "Press a key to begin", 18, WIDTH / 2, HEIGHT * 3 / 4)
    pg.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg,quit()
            if event.type == pg.KEYUP:
                waiting = False
    
# load all game graphics
background = pg.image.load(path.join(img_dir, "skynight.png")).convert()
background_rect = background.get_rect()
player_img = pg.image.load(path.join(img_dir, "plane.gif")).convert()
player_mini_img = pg.transform.scale(player_img, (30, 30))
player_mini_img.set_colorkey(WHITE)
bullet_img = pg.image.load(path.join(img_dir, "bulletvertical.png")).convert()
towers_images = []
towers_list = ['tower 1.png', 'tower 2.png', 'both_towers.png']
for img in towers_list:
    towers_images.append(pg.image.load(path.join(img_dir, img)).convert())

explosion_anim = {}
explosion_anim['lg'] = []
explosion_anim['sm'] = []
explosion_anim['player'] = []
for i in range (11):
    filename = 'explosion{}.png'.format(i)
    img = pg.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    img_lg = pg.transform.scale(img, (75, 75))
    explosion_anim['lg'].append(img_lg)
    img_sm = pg.transform.scale(img, (32, 32))
    explosion_anim['sm'].append(img_sm)
    img_player = pg.transform.scale(img, (100, 100))
    explosion_anim['player'].append(img)
powerup_images = {}
powerup_images['shield'] = pg.image.load(path.join(img_dir, 'shield_gold.png')).convert()
powerup_images['gun'] = pg.image.load(path.join(img_dir, 'bolt_gold.png')).convert()

# load all game sounds
shoot_sound = pg.mixer.Sound(path.join(snd_dir, 'yippee-tbh.wav'))
shield_sound = pg.mixer.Sound(path.join(snd_dir, 'nut.wav'))
power_sound = pg.mixer.Sound(path.join(snd_dir, 'nut.wav'))
shoot_sound.set_volume(0.2)
shield_sound.set_volume(1)
power_sound.set_volume(1)
expl_sounds = []
for snd in ['metal-pipe-clang.wav']:
    expl_sounds.append(pg.mixer.Sound(path.join(snd_dir, snd)))
player_die_sound = pg.mixer.Sound(path.join(snd_dir, 'bingchilling.ogg'))
for snd in expl_sounds:
    snd.set_volume(0.1)

pg.mixer.music.load(path.join(snd_dir, 'never.ogg'))
pg.mixer.music.set_volume(1)

pg.mixer.music.play(loops = -1)
# Game loop
game_over = True
running = True
while running:
    if game_over:
        show_go_screen()
        game_over = False
        all_sprites = pg.sprite.Group()
        bullets = pg.sprite.Group()
        powerups = pg.sprite.Group()
        mobs = pg.sprite.Group()
        player = Player()
        all_sprites.add(player)
        for i in range (8):
            newmob()

        score = 0
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pg.event.get():
        # check for closing window
        if event.type == pg.QUIT:
            running = False

    # Update
    all_sprites.update()

    # check to see if bullet hit the mob
    hits = pg.sprite.groupcollide(mobs, bullets, True, True)  
    for hit in hits:
        score += 1
        random.choice(expl_sounds).play()
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        if random.random() > 0.9:
            pow = Pow(hit.rect.center)
            all_sprites.add(pow)
            powerups.add(pow)
        newmob()

    # check to see if mob hit the player
    hits = pg.sprite.spritecollide(player, mobs, True, pg.sprite.collide_circle)
    for hit in hits:
        player.shield -= 1
        expl = Explosion(hit.rect.center, 'sm')
        all_sprites.add(expl)
        newmob()
        if player.shield <= 0:
            player_die_sound.play()
            death_explosion = Explosion(player.rect.center, 'player')
            all_sprites.add(death_explosion)
            player.hide()
            player.lives -= 1
            player.shield = 3
            
    #check to see if player hit powerup
    hits = pg.sprite.spritecollide(player, powerups, True)
    for hit in hits:
        if hit.type == 'shield':
            player.shield += 1
            shield_sound.play()
            if player.shield >= 3:
                player.shield = 3
        if hit.type == 'gun':
            player.powerup()
            power_sound.play()


    #if the player died and the explosion has finished playing
    if player.lives == 0 and not death_explosion.alive():
        game_over = True

    # Draw / render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    draw_text(screen, str(score), 18, WIDTH / 2, 10)
    draw_shield_bar(screen, 5, 5, player.shield)
    draw_lives(screen, WIDTH - 100, 5, player.lives, player_mini_img)
    # *after* drawing everything, flip the display
    pg.display.flip()

pg.quit()