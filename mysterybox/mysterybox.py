import pygame
import random
from os import path

img_dir = path.join(path.dirname(__file__), 'img')

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mystery Box")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images
closed_box_img = pygame.image.load(path.join(img_dir, "closed_box.png")).convert()
closed_box_img.set_colorkey(BLACK)
open_box_img = pygame.image.load(path.join(img_dir, "open_box.png")).convert()
open_box_img.set_colorkey(BLACK)
treasure_img = pygame.image.load(path.join(img_dir, "treasure.png")).convert()
treasure_img.set_colorkey(BLACK)

# Set box position
box_x = (width - closed_box_img.get_width()) // 2
box_y = (height - closed_box_img.get_height()) // 2

# Set initial game state
game_over = False
box_opened = False

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN and not box_opened:
            mouse_pos = pygame.mouse.get_pos()
            box_rect = pygame.Rect(box_x, box_y, closed_box_img.get_width(), closed_box_img.get_height())
            if box_rect.collidepoint(mouse_pos):
                box_opened = True

    # Fill the screen with the background color
    screen.fill(WHITE)

    if box_opened:
        screen.blit(open_box_img, (box_x, box_y))
        screen.blit(treasure_img, (box_x + 30, box_y + 30))
    else:
        screen.blit(closed_box_img, (box_x, box_y))

    # Update the display
    pygame.display.update()

# Quit the game
pygame.quit()

