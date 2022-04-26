import pygame
pygame.init()

# killer objects
KILLER_LONG = pygame.image.load("assets/images/killer1.png")
KILLER_BOX = pygame.image.load("assets/images/killer2.png")


class Killer():

    # define images for the two killer types
    TYPE_MAP = {
        "long": (KILLER_LONG),
        "box": (KILLER_BOX),
    }

    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.killer_img = self.TYPE_MAP[type]
        self.rect = self.killer_img.get_rect()
        self.rect.center = (x, y)

    def draw(self, window, player):

        # checking for collisions
        collide = False
        if self.rect.colliderect(player):
            collide = True

        window.blit(self.killer_img, (self.rect.x, self.rect.y))

        return collide

    def move(self, velocity):
        self.rect.y += velocity
