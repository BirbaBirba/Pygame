import pygame, sys
from scene import Scene
from setup import scene
from settings import *

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("snake")
clock = pygame.time.Clock()
scene = Scene(scene, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    scene.run()
    clock.tick(60)
