import pygame
from pygame.locals import *
import sys
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
running = True

player = pygame.image.load("E:/python/projek/tutorial-pygame-master/resources/images/dude.png")
playpos = [100, 200]

musuh = pygame.image.load("E:/python/projek/tutorial-pygame-master/resources/images/badguy.png")
x_musuh = random.randint(400, 800)
y_musuh = random.randint(1, 550)
muspos = [[x_musuh, y_musuh]]
waktu = 100

while running:
    screen.fill(0)
    screen.blit(player, playpos)

    waktu -= 1
    if waktu == 0:
        muspos.append([x_musuh, random.randint(50, y_musuh )])
        waktu = 100
    for enemi in muspos:
        enemi[0] -= 2
        if enemi[0] == 0:
            muspos.pop(0)
    for enemi in muspos:
        screen.blit(musuh, (enemi[0], enemi[1]))  # Memindahkan pemindahan musuh ke dalam loop utama
    pygame.display.flip()
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            muspos.pop(0)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and playpos[0] > 0:
            playpos[0] -= 10
        elif keys[pygame.K_RIGHT] and playpos[0] < 700:
            playpos[0] += 10
        elif keys[pygame.K_UP] and playpos[1] > 0:
            playpos[1] -= 10
        elif keys[pygame.K_DOWN] and playpos[1] < 500:
            playpos[1] += 10


        # Memperbarui posisi musuh secara acak setiap frame

