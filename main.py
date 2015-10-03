import pygame
import game


background_color = (0, 0, 0)  # black
width, height = 800, 800
caption = "RPG Game"

if __name__ == "__main__":
    game = game.Game({"background_color": background_color,
                      "width": width,
                      "height": height,
                      "caption": caption})
    running = True
    while running:
        for event in pygame.event.get():  # EVENT LOOP!
            if event.type == pygame.QUIT:
                running = False
