import pygame
import sys

pygame.init()

display_size=[1540,800]
display = pygame.display.set_mode(display_size)

game = True
end = False

block_size = 20

def load_map(map):
    f = open(map, 'r')
    data = f.read()
    f.close()
    data = data.split('\n')
    game_map = []
    for row in data:
        game_map.append(list(row))

    return game_map


world_map = load_map('map.txt')

def draw_grid():
    for i in range(display_size[0] // block_size):
        pygame.draw.line(display, (255,255,255), (i * block_size, 0), (i * block_size, display_size[1]))
    for i in range(display_size[0] // block_size):
        pygame.draw.line(display, (255,255,255), (0, i * block_size), (display_size[0], i * block_size))


def me ():
    global me, me_an_1, me_an_2, me_an_3, me_an_4,me_an_5
    me = pygame.image.load('img/enemy_an_0.png')
    me_an_1 = pygame.image.load('img/enemy_an_1.png')
    me_an_2 = pygame.image.load('img/enemy_an_2.png')
    me_an_3 = pygame.image.load('img/enemy_an_3.png')
    me_an_4 = pygame.image.load('img/enemy_an_4.png')
    me_an_5 = pygame.image.load('img/enemy_an_5.png')




def update():
    pygame.display.update()


while game:

    update()
    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            game = end



