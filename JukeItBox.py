# libs/other
import pygame
import random
import sys
# components
import button_class
import player_control
import killer_class

pygame.init()
pygame.mixer.init()
pygame.font.init()
clock = pygame.time.Clock()

# ------------------------------- SETTINGS -----------------------------------------

# window
FPS = 120
WIN_WIDTH, WIN_HEIGHT = 720, 720
WINDOW = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
FONT = pygame.font.SysFont('consolas', 40)
WIN_FONT = pygame.font.SysFont('consolas', 80)
pygame.display.set_caption('JukeItBox')
ICON_IMG = pygame.image.load("assets/images/killer2.png")
pygame.display.set_icon(ICON_IMG)

# sounds
CLICK_SOUND = pygame.mixer.Sound("assets/sounds/click.mp3")
CLICK_SOUND.set_volume(0.2)
MUSIC = pygame.mixer.Sound("assets/sounds/music1.mp3")
MUSIC.set_volume(0.2)
DEATH_SOUND = pygame.mixer.Sound("assets/sounds/death.mp3")
DEATH_SOUND.set_volume(0.2)
GOAL_SOUND = pygame.mixer.Sound("assets/sounds/goal.mp3")
GOAL_SOUND.set_volume(0.2)

# custom cursor
pygame.mouse.set_visible(False)
CURSOR_IMG = pygame.image.load("assets/images/cursor.png")
CURSOR_IMG_RECT = CURSOR_IMG.get_rect()

# images
ARROWKEYS_IMG = pygame.image.load("assets/images/arrowkeys.png")
LOGO = pygame.image.load("assets/images/junkitbox_logo.png")
PLAYER_IMG = pygame.transform.scale(pygame.image.load(
    "assets/images/player_cube_pink.png"), (30, 30))
GOAL_IMG = pygame.image.load("assets/images/goal.png")
START_IMG = pygame.image.load("assets/images/start_img.png").convert_alpha()
EXIT_IMG = pygame.image.load("assets/images/exit_img.png").convert_alpha()
RESTART_IMG = pygame.image.load(
    "assets/images/restart_img.png").convert_alpha()

# game variables
VELOCITY = 5
ENEMY_VELOCITY = 4
killers = []
killer_count = 100

# ------------------------------- IN-GAME -----------------------------------------


def draw_game(player, goal):
    # background (color)
    WINDOW.fill((30, 30, 30))

    # draw killers
    for killer in killers:
        killer_class.Killer.draw(killer, WINDOW, player)

    # draw goal
    WINDOW.blit(GOAL_IMG, (0, goal.y))

    # draw player
    WINDOW.blit(PLAYER_IMG, (player.x, player.y))

    pygame.display.update()


def game():
    # define player rect
    P_WIDTH, P_HEIGHT = PLAYER_IMG.get_width(), PLAYER_IMG.get_height()
    player = pygame.Rect(
        WIN_WIDTH/2 - P_WIDTH/2, WIN_HEIGHT/2 - P_HEIGHT/2, P_WIDTH, P_HEIGHT)

    goal = pygame.Rect(0, -14200, GOAL_IMG.get_width(), GOAL_IMG.get_height())

    # create some killers
    if len(killers) == 0:
        for i in range(killer_count):
            while True:
                # random value from range for x and y coordinates
                x, y = random.randrange(
                    50, WIN_WIDTH - 50), random.randrange(-14000, -500)
                new_rect = pygame.Rect(x, y, 100, 200)

                # previous method of creating killers (no collision check)
                # killer = killer_class.Killer(
                # random.randrange(x),
                # random.randrange(y),
                # random.choice(["box", "long"]))

                # check created killer collides with any other killers, if so break
                if not any(killer for killer in killers if new_rect.colliderect(killer.x, killer.y, 100, 200)):
                    break
            new_killer = killer_class.Killer(
                x, y, random.choice(["box", "long"]))
            killers.append(new_killer)

    run = True
    MUSIC.play()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()

        # killer movement
        for killer in killers:
            killer_class.Killer.move(killer, ENEMY_VELOCITY)
            # hit detection
            if killer_class.Killer.draw(killer, WINDOW, player):
                DEATH_SOUND.play()
                run = False
                MUSIC.stop()
                lost()

        # player movement
        keys_pressed = pygame.key.get_pressed()
        player_control.handle_player_movement(
            keys_pressed, player, VELOCITY, WIN_WIDTH, WIN_HEIGHT)

        # goal
        goal.y += ENEMY_VELOCITY
        if player.colliderect(goal):
            GOAL_SOUND.play()
            run = False
            MUSIC.stop()
            win()

        # render game objects
        draw_game(player, goal)

# ------------------------------- WIN -----------------------------------------


def draw_win():
    WINDOW.fill((30, 30, 30))

    # text
    win_text = WIN_FONT.render("nice", 1, (220, 220, 220))
    WINDOW.blit(win_text, (WIN_WIDTH/2 - win_text.get_width()/2, 200))

    # restart button
    restart_button = button_class.Button(
        WIN_WIDTH/2 - RESTART_IMG.get_width()/2, 400, RESTART_IMG)

    if restart_button.draw(WINDOW):
        CLICK_SOUND.play()
        reset()

    # exit button
    exit_button = button_class.Button(
        WIN_WIDTH/2 - EXIT_IMG.get_width()/2, 550, EXIT_IMG)

    if exit_button.draw(WINDOW):
        CLICK_SOUND.play()
        sys.exit()

    # cursor
    WINDOW.blit(CURSOR_IMG, CURSOR_IMG_RECT)

    pygame.display.update()


def win():
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()

        # set custom cursor on top of mouse
        CURSOR_IMG_RECT.topleft = pygame.mouse.get_pos()

        draw_win()

# ------------------------------- LOST -----------------------------------------


def draw_lost():
    WINDOW.fill((30, 30, 30))

    # restart button
    restart_button = button_class.Button(
        WIN_WIDTH/2 - RESTART_IMG.get_width()/2, 200, RESTART_IMG)

    if restart_button.draw(WINDOW):
        CLICK_SOUND.play()
        reset()

    # text
    hint_text = FONT.render("better luck next time :(", 1, (220, 220, 220))
    WINDOW.blit(hint_text, (WIN_WIDTH/2 - hint_text.get_width()/2, 450))

    # image
    WINDOW.blit(LOGO, (WIN_WIDTH/2 - LOGO.get_width()/2, 50))

    # cursor
    WINDOW.blit(CURSOR_IMG, CURSOR_IMG_RECT)

    pygame.display.update()


def lost():
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()

        # set custom cursor on top of mouse
        CURSOR_IMG_RECT.topleft = pygame.mouse.get_pos()

        draw_lost()


# reset the game
def reset():
    global killers
    killers = []
    game()

# ------------------------------- MENU -----------------------------------------


def draw_menu():
    WINDOW.fill((30, 30, 30))

    # start button
    start_button = button_class.Button(
        WIN_WIDTH/2 - START_IMG.get_width()/2, 200, START_IMG)

    if start_button.draw(WINDOW):
        CLICK_SOUND.play()
        game()

    # text
    controls_text = FONT.render("arrow keys to move", 1, (220, 220, 220))
    hint_text = FONT.render("HINT: DONT HIT ANY OBJECTS", 1, (220, 220, 220))
    WINDOW.blit(controls_text, (WIN_WIDTH/2 -
                controls_text.get_width()/2, 540))
    WINDOW.blit(hint_text, (WIN_WIDTH/2 - hint_text.get_width()/2, 650))

    # images
    WINDOW.blit(LOGO, (WIN_WIDTH/2 - LOGO.get_width()/2, 50))
    WINDOW.blit(ARROWKEYS_IMG, (WIN_WIDTH/2 -
                ARROWKEYS_IMG.get_width()/2, 380))

    # cursor
    WINDOW.blit(CURSOR_IMG, CURSOR_IMG_RECT)

    pygame.display.update()


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()

        CURSOR_IMG_RECT.topleft = pygame.mouse.get_pos()

        clock.tick(FPS)

        draw_menu()


if __name__ == "__main__":
    main()
