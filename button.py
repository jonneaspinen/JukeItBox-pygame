import pygame
pygame.init()


class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, window):
        action = False
        m_pos = pygame.mouse.get_pos()
        # check if the mouse cursor in on the button
        if self.rect.collidepoint(m_pos):
            # if left mouse (=[0]) is clicked, make 'clicked' True
            # we have the 'clicked' variable, because 'get_pressed' registers multiple
            # clicks with only one click, this way we restrict it to only register once
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        # when left mouse is not pressed, 'clicked' goes back to False
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        window.blit(self.image, (self.rect.x, self.rect.y))

        return action
