import pygame
import random

pygame.init()


window = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Target Practice")
icon = pygame.image.load('moon.png')
pygame.display.set_icon(icon)


targ = pygame.image.load('Target.png')
x = random.randint(0, 300)
y = random.randint(0, 200)
white = (255, 255, 255)
black = (0, 0, 0)


def Target():
    window.blit(targ, (x, y))


Score = 0
running = True

while running:
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(str(Score), True, white, black)
    textRect = text.get_rect()
    textRect.center = (400, 50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            quit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()


            if x + 257 < int(str(pos[0])) < x + 546 and y + 83 < int(str(pos[1])) < y + 370:
                if x + 292 < int(str(pos[0])) < x + 517 and y + 131 < int(str(pos[1])) < y + 651:
                    window.fill((0,0,0))
                    x = random.randint(0, 300)
                    y = random.randint(0, 200)
                    Score += 1

            else:
                Score -= 1

    Target()
    window.blit(text, textRect)
    pygame.display.update()

