import sys
import pygame

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
clock = pygame.time.Clock()

def player_animation():
    global player_at_ceiling, player_y_speed
    player.x += player_x_speed
    if player_at_ceiling == False:
        player.y -= player_y_speed
        if player.top < 675:
            player_at_ceiling = True
    else:    
        player.y += player_y_speed

    if player.colliderect(floor):
        player_y_speed = 0
        player_at_ceiling = False

screen_width = 1280
screen_height = 960
player_x_speed = 0
player_y_speed =0
player_at_ceiling = False
player_at_floor = False

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Mar10')

player = pygame.Rect(50, 775, 50, 85)
floor = pygame.Rect(0,860,screen_width,100)

bg_colour = pygame.Color('grey12')
light_grey = (200, 200, 200)
green = (0, 255, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_x_speed += 7
            if event.key == pygame.K_LEFT:
                player_x_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player_x_speed -= 7
            if event.key == pygame.K_LEFT:
                player_x_speed += 7
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                #no double jumping bro!
                if player_y_speed == 0:
                    player_y_speed += 7

    player_animation()

    screen.fill(bg_colour)
    pygame.draw.rect(screen, green, floor)
    pygame.draw.rect(screen, light_grey, player)
   
    pygame.display.flip()
    clock.tick(60)