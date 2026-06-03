import pygame
from sys import exit

Game_Width = 360
Game_Height = 640

background_image = pygame.image.load("flappybirdbg.png")

def draw():
    window.blit(background_image,(0,0))

pygame.init()
window = pygame.display.set_mode((Game_Width,Game_Height))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    draw()
    pygame.display.update()
    clock.tick(60)

