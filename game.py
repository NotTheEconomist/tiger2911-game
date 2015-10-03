import pygame
import pygame.locals


class Game(object):
    def __init__(self, **pygame_options):
        w_dimensions = (pygame_options.get("width"), pygame_options.get("height"))
        width, height = w_dimensions
        background_color = pygame_options.get("background_color")
        caption = pygame_options.get("caption")

        self.screen = pygame.display.set_mode(w_dimensions)
        self.screen.fill(background_color)
        pygame.display.set_caption(caption)
        self.players = []

    def register_player(self, player):
        self.players.append(player)
