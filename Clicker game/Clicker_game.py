#idle clicker game
import pygame as pg
from os import path
pg.init()

img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')

#colour libary
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
purple = (127, 0, 255)
orange = (255, 165, 0)

#screen display
screen = pg.display.set_mode([300, 450])
pg.display.set_caption('idle clicker game')
framerate = 60
font = pg.font.Font('freesansbold.ttf', 16)
timer = pg.time.Clock()

#game variables
#values
green_value = 1
red_value = 2
orange_value = 3
white_value = 4
purple_value = 5

#draw bar
draw_green = False
draw_red = False
draw_orange = False
draw_white = False
draw_purple = False

#length of bar
green_length = 0
red_length = 0
orange_length = 0
white_length = 0
purple_length = 0

#speed of bar
green_speed = 5
red_speed = 4
orange_speed = 3
white_speed = 2
purple_speed = 1

#global score
score = 0

#draw button function
green_cost = 1
green_owned = False
green_manager_cost = 100
red_cost = 2
red_owned = False
red_manager_cost = 500
orange_cost = 3
orange_owned = False
orange_manager_cost = 1000
white_cost = 4
white_owned = False
white_manager_cost = 4000
purple_cost = 5
purple_owned = False
purple_manager_cost = 10000


def draw_task(color, y_coord, value, draw, length, speed):
    global score
    if draw and length < 200:
        length += speed
    elif length >= 200:
        draw = False
        length = 0
        score += value

    task = pg.draw.circle(screen, color, (36, y_coord), 26, 5)
    pg.draw.rect(screen, color, [70, y_coord - 15, 200, 30])
    pg.draw.rect(screen, black, [75, y_coord - 10, 190, 20])
    pg.draw.rect(screen, color, [70, y_coord - 15, length, 30])
    value_text = font.render(str(round(value,2)), True, white)
    screen.blit(value_text, (16, y_coord - 10))
    return task, length, draw


def draw_buttons(color, x_coord, cost, owned, manager_cost):
    color_button = pg.draw.rect(screen, color, [x_coord, 340, 50, 30])
    color_cost = font.render(str(round(cost, 2)), True, black)
    screen.blit(color_cost, (x_coord + 6, 350))
    if not owned:
        manager_button = pg.draw.rect(screen, color, [x_coord, 405, 50, 30])
        manager_text = font.render(str(round(manager_cost, 2)), True, black)
        screen.blit(manager_text, (x_coord + 2, 410))
    else:
        manager_button = pg.draw.rect(screen, black, [x_coord, 405, 50, 30])
    return color_button, manager_button

# load all game graphics
background = pg.image.load(path.join(img_dir, "sky.png")).convert()
background_rect = background.get_rect()
taks1 = pg.image.load(path.join(img_dir, "sky.png")).convert()
task2 = pg.image.load(path.join(img_dir, "sky.png")).convert()
task3 = pg.image.load(path.join(img_dir, "sky.png")).convert()
task4 = pg.image.load(path.join(img_dir, "sky.png")).convert()
task5 = pg.image.load(path.join(img_dir, "sky.png")).convert()





#game running/quit game
running = True
while running:
    timer.tick(framerate)
    #managers button 
    if green_owned and not draw_green:
        draw_green = True
    if red_owned and not draw_red:
        draw_red = True
    if orange_owned and not draw_orange:
        draw_orange = True
    if white_owned and not draw_white:
        draw_white = True
    if purple_owned and not draw_purple:
        draw_purple = True
    #events run quit game
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        #event click tasks    
        if event.type == pg.MOUSEBUTTONDOWN:
            if task1.collidepoint(event.pos):
                draw_green = True
            if task2.collidepoint(event.pos):
                draw_red = True
            if task3.collidepoint(event.pos):
                draw_orange = True
            if task4.collidepoint(event.pos):
                draw_white = True
            if task5.collidepoint(event.pos):
                draw_purple = True
            #event manager buy
            if green_manager_buy.collidepoint(event.pos) and score >= green_manager_cost and not green_owned:
                green_owned = True
                score -= green_manager_cost
            if red_manager_buy.collidepoint(event.pos) and score >= red_manager_cost and not red_owned:
                red_owned = True
                score -= red_manager_cost
            if orange_manager_buy.collidepoint(event.pos) and score >= orange_manager_cost and not orange_owned:
                orange_owned = True
                score -= orange_manager_cost
            if white_manager_buy.collidepoint(event.pos) and score >= white_manager_cost and not white_owned:
                white_owned = True
                score -= white_manager_cost
            if purple_manager_buy.collidepoint(event.pos) and score >= purple_manager_cost and not purple_owned:
                purple_owned = True
                score -= purple_manager_cost
            #event buy upgrade
            if green_buy.collidepoint(event.pos) and score >= green_cost:
                green_value += .15
                score -= green_cost
                green_cost += .1
            if red_buy.collidepoint(event.pos) and score >= red_cost:
                red_value += .3
                score -= red_cost
                red_cost += .2
            if orange_buy.collidepoint(event.pos) and score >= orange_cost:
                orange_value += .45
                score -= orange_cost
                orange_cost += .3
            if white_buy.collidepoint(event.pos) and score >= white_cost:
                white_value += .6
                score -= white_cost
                white_cost += .4
            if purple_buy.collidepoint(event.pos) and score >= purple_cost:
                purple_value += .75
                score -= purple_cost
                purple_cost += .5
                


    # displays whats on the screen
    screen.fill(black)
    screen.blit(background, background_rect)
    task1, green_length, draw_green = draw_task(green, 50, green_value, draw_green, green_length, green_speed)
    task2, red_length, draw_red =draw_task(red, 110, red_value, draw_red, red_length, red_speed)
    task3, orange_length, draw_orange =draw_task(orange, 170, orange_value, draw_orange, orange_length, orange_speed)
    task4, white_length, draw_white =draw_task(white, 230, white_value, draw_white, white_length, white_speed)
    task5, purple_length, draw_purple =draw_task(purple, 290, purple_value, draw_purple, purple_length, purple_speed)
    #manager upgrades
    green_buy, green_manager_buy = draw_buttons(green, 10,  green_cost, green_owned, green_manager_cost)
    red_buy, red_manager_buy = draw_buttons(red, 70,  red_cost, red_owned, red_manager_cost)
    orange_buy, orange_manager_buy = draw_buttons(orange, 130,  orange_cost, orange_owned, orange_manager_cost)
    white_buy, white_manager_buy = draw_buttons(white, 190,  white_cost, white_owned, white_manager_cost)
    purple_buy, purple_manager_buy = draw_buttons(purple, 250,  purple_cost, purple_owned, purple_manager_cost)

    #score for money
    display_score = font.render('Money: £'+str(round(score, 2)), True, white, black)
    screen.blit(display_score, (10, 5))
    buy_more = font.render('Buy More', True, white)
    screen.blit(buy_more, (10, 315))
    buy_managers = font.render('Buy Managers', True, white)
    screen.blit(buy_managers, (10, 380))
    pg.display.flip()
pg.quit()