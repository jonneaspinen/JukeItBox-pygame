import pygame


def handle_player_movement(keys_pressed, player, VELOCITY, WIN_WIDTH, WIN_HEIGHT):
    if keys_pressed[pygame.K_LEFT] and player.x - VELOCITY > 0:
        player.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT] and player.x + VELOCITY + player.width < WIN_WIDTH:
        player.x += VELOCITY
    if keys_pressed[pygame.K_UP] and player.y - VELOCITY > 0:
        player.y -= VELOCITY
    if keys_pressed[pygame.K_DOWN] and player.y + VELOCITY + player.height < WIN_HEIGHT:
        player.y += VELOCITY
