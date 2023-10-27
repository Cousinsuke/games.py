import pygame as pg
pg.init() 
font = pg.font.Font('freesansbold.ttf', 24) #font 
screen = pg.display.set_mode([800, 500]) # screen display
timer = pg.time.Clock()
messages = ['The message to display!!!',
            'The message to display!!!',
            'The message to display!!!']
snip = font.render('', True, 'white')
counter = 0
speed = 3
active_messsage = 0
message = messages[active_messsage]
done = False

run = True
while run:
    screen.fill('dark grey') 
    timer.tick(60)
    pg.draw.rect(screen, 'black', [0, 300, 800, 200]) #makes box for text
    if counter < speed * len(message):
        counter += 1
    elif counter >= speed * len(message):
        done = True

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN and done and active_messsage < len(messages) - 1:
                active_messsage += 1
                done = False
                message = messages[active_messsage]
                counter = 0


    snip = font.render(message[0:counter//speed], True, 'white')
    screen.blit(snip, (10, 310))

    pg.display.flip()
pg.quit()