import pygame
from sys import exit

Game_Width = 360
Game_Height = 640

bird_y=Game_Height/8
bird_x=Game_Width/2
bird_width=34
bird_height=24

class Bird(pygame.Rect):
    def __init__(self, img):
        pygame.Rect.__init__(self, bird_x, bird_y, bird_height, bird_width)
        self.img=img    




background_image = pygame.image.load("flappybirdbg.png")
bird_image=pygame.image.load("flappybird.png")
bird_image=pygame.transform.scale(bird_image, (bird_width, bird_height))

bird=Bird(bird_image)

def draw():
    window.blit(background_image,(0,0))
    window.blit(bird.img,bird)

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

