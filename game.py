# Bouncing ball game
# Author - Indranil Ray

import sys
import pygame

pygame.init()

#size of display window
size = width, height = 600, 500
background = 255, 255, 255

ball_speed = [1, 1]
plate_speed = 40

#action key for K_RIGHT and K_LEFT arrow
key = [False, False]
delay_t = 10
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bouncing ball")

ball = pygame.image.load("ball.jpg")
ballrect = ball.get_rect()
plate = pygame.image.load("plate.png")
platerect = plate.get_rect()
#set initial plate position
platerect = platerect.move(275, 490)

#game loop
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                key[0] = True
            elif event.key == pygame.K_LEFT:
                key[1] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                key[0] = False
            elif event.key == pygame.K_LEFT:
                key[1] = False
        if platerect.right < width + plate_speed:
         if key[0]:
             platerect = platerect.move(plate_speed, 0)
        if platerect.left > -plate_speed:
         if key[1]:
             platerect = platerect.move(-plate_speed, 0)


    ballrect = ballrect.move(ball_speed)
    if pygame.Rect.colliderect(ballrect, platerect):
        ball_speed[1] = -ball_speed[1]
        if delay_t > 3:
            delay_t -= 1
    if ballrect.bottom > height:
        sys.exit(1)
    if ballrect.left < 0 or ballrect.right > width:
        ball_speed[0] = -ball_speed[0]
    if ballrect.top < 0 :
        ball_speed[1] = -ball_speed[1]

    pygame.time.delay(delay_t)
    screen.fill(background)
    screen.blit(ball, ballrect)
    screen.blit(plate, platerect)
    pygame.display.flip()
