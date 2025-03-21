import sys
import pygame

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
clock = pygame.time.Clock()

def player_animation():
    global player_y_speed, gravity, player_inflight, player_thrust
    
    player.x += player_x_speed

    if (player_thrust > 0 and player_inflight):
        player.y -= player_y_speed
        player_thrust -= 1
    else:
        player.y += player_y_speed

    if player.colliderect(floor):
        player_y_speed = 0
        #add the floor bounce correction - fix this later!
        player.y = player.y - 1
        player_thrust = 20
        player_at_ceiling = False
        player_inflight = False

screen_width = 1280
screen_height = 960
player_x_speed = 0
player_y_speed = 0
player_thrust = 20
player_horizontal_momentum = 7
player_vertical_momentum = 7
player_inflight = False

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
                player_x_speed += player_horizontal_momentum
            if event.key == pygame.K_LEFT:
                player_x_speed -= player_horizontal_momentum
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player_x_speed -= player_horizontal_momentum
            if event.key == pygame.K_LEFT:
                player_x_speed += player_horizontal_momentum
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                #no double jumping bro!
                if player_inflight == False:
                    player_inflight = True
                    player_y_speed += player_vertical_momentum

    player_animation()

    screen.fill(bg_colour)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, green, floor)
    
   
    pygame.display.flip()
    clock.tick(60)