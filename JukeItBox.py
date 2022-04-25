from msilib.schema import Class
import pygame
import button

pygame.init()
pygame.mixer.init()
pygame.font.init()

# window
FPS = 60
WIN_WIDTH, WIN_HEIGHT = 1280, 720
WINDOW = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('JukeItBox')
FONT = pygame.font.SysFont('consolas', 40)

# sounds
CLICK_SOUND = pygame.mixer.Sound("assets/sounds/click.mp3")
CLICK_SOUND.set_volume(0.1)

MUSIC = pygame.mixer.Sound("assets/sounds/music1.mp3")
MUSIC.set_volume(0.1)

# setting variables
VELOCITY = 10

#------------------------------------------------------------------------------

# player object
PLAYER_IMAGE = pygame.image.load("assets/images/player_cube_pink.png")
P_WIDTH, P_HEIGHT = PLAYER_IMAGE.get_width(), PLAYER_IMAGE.get_height()
PLAYER = PLAYER_IMAGE

# killbox objects
KBOX_THIN = pygame.Rect(KBOX_START_W, KBOX_START_H, )
KBOX = pygame.Rect

# player controlling
def handle_player_movement(keys_pressed, player):
    if keys_pressed[pygame.K_LEFT] and player.x - VELOCITY > 0:
        player.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT] and player.x + VELOCITY + player.width < WIN_WIDTH:
        player.x += VELOCITY
    if keys_pressed[pygame.K_UP] and player.y - VELOCITY > 0:
        player.y -= VELOCITY
    if keys_pressed[pygame.K_DOWN] and player.y + VELOCITY + player.height < WIN_HEIGHT:
        player.y += VELOCITY

def draw_game(player):
    WINDOW.fill((30, 30, 30))
    WINDOW.blit(PLAYER, (player.x, player.y))
    pygame.display.update()

#------------------------------------------------------------------------------

# Custom cursor
pygame.mouse.set_visible(False)
CURSOR_IMG = pygame.image.load("assets/images/cursor.png")
CURSOR_IMG_RECT = CURSOR_IMG.get_rect()

# start button
start_img = pygame.image.load("assets/images/start_img.png").convert_alpha()
start_button = button.Button(WIN_WIDTH/2 - start_img.get_width()/2, 200, start_img)

# extra images
ARROWKEYS_IMG = pygame.image.load("assets/images/arrowkeys.png")

def draw_menu():
    WINDOW.fill((30, 30, 30))

    if start_button.draw(WINDOW):
        CLICK_SOUND.play()
        game()
        
    controls_text = FONT.render("arrow keys to move", 1, (220, 220, 220))
    WINDOW.blit(controls_text, (WIN_WIDTH/2 - controls_text.get_width()/2, 650))
    WINDOW.blit(ARROWKEYS_IMG, (WIN_WIDTH/2 - ARROWKEYS_IMG.get_width()/2, 450))
    WINDOW.blit(CURSOR_IMG, CURSOR_IMG_RECT)

    pygame.display.update()

#------------------------------------------------------------------------------

def game():
    player = pygame.Rect(WIN_WIDTH/2 - P_WIDTH/2, WIN_HEIGHT/2 - P_HEIGHT/2, P_WIDTH, P_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    MUSIC.play()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        keys_pressed = pygame.key.get_pressed()
        handle_player_movement(keys_pressed, player)

        draw_game(player)

        clock.tick(FPS)

#------------------------------------------------------------------------------

def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        CURSOR_IMG_RECT.topleft = pygame.mouse.get_pos()

        clock.tick(FPS)

        draw_menu()


if __name__ == "__main__":
    main()