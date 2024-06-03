import pygame as pg
from os import path

img_dir = path.join(path.dirname(__file__), 'img')

pg.init() 
font = pg.font.Font('freesansbold.ttf', 24)  # font 
screen = pg.display.set_mode([800, 500])  # screen display
timer = pg.time.Clock()
messages = [
    'dayyyy oooo dayyy ooo',
    'daylight come and we bomb your homes',
    'dayyyyy oooo dayyy ooooo',
    'the first afghani royal air show',
    'hey mr taliban hand over bing laden',
    'daylight come and we bomb your home',

    'he never has a shave',
    'and hes always in pyjamas',
    'daylight come and we bomb your home',

    'the afghan women are all in a rush',
    'daylight come and we bomb your home',

    'to shave their fannys coz they dont like bush!',
    'daylight come and we bomb your home',

    'and the cornish SAS broke down debhanems door!',
    'daylight come and we bomb your home',

    'because they heard ben linen was on the third floor!',
    'daylight come and we bomb your home',

    'now you think youre safe in the cave that youre sat!',
    'daylight come and we bomb your home',

    'but remember hiroshima you big daft twat!',
    'daylight come and we bomb your home',

    'now come tommorow youll soon be crying',
    'daylight come and we bomb your home',

    'because rumsfelts brother was a new york fireman!',
    'daylight come and we bomb your home',

    'hey! mr yankee man why cant you find him',
    'it cant that bloody hard',
    'he lives in a cave and ***** in a ******* bucket',
    'not clever is he?',

    'daylight come and we bomb yoooooooooooooooour homeeeeeeeeeeeeee',]

snip = font.render('', True, 'white')
counter = 0
speed = 3
active_message = 0
message = messages[active_message]
done = False

# Load background image and adjust its size to fit within the screen
background = pg.transform.scale(pg.image.load(path.join(img_dir, 'osama.png')).convert_alpha(), (800, 370))

run = True
while run:
    screen.fill((255, 255, 255))  # Fill the screen with white color
    screen.blit(background, (0, 0)) 
    timer.tick(60)
    pg.draw.rect(screen, 'black', [0, 370, 800, 200])  # makes box for text

    if counter < speed * len(message):
        counter += 1
    elif counter >= speed * len(message):
        done = True
        if active_message < len(messages) - 1:
            active_message += 1
            message = messages[active_message]
            counter = 0
            done = False

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    snip = font.render(message[0:counter//speed], True, 'white')
    screen.blit(snip, (0, 375))
    pg.display.flip()
pg.quit()
