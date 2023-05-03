import pygame
import os
from PykemonOptionsMenu import PykemonOptionsMenu


class PykemonMenu:
    def __init__(self, width, height):

        # Set the Width and the Height
        self.width = width
        self.height = height

        # Background Colors
        self.sky_color = pygame.image.load(os.path.join('MenuSimulator/Assets', 'Pykemon_Background.png')) # Pykemon Background Image

        # Set font size for buttons and for the Title Text
        self.button_font = pygame.font.SysFont('Arial', 32)
        self.title_font = pygame.font.SysFont('calibri', 96)

        # Set up buttons
        self.button_width = 200
        self.button_height = 50
        self.button_spacing = 20

        self.start_button = pygame.Rect((self.width - self.button_width) / 2, 400, self.button_width, self.button_height)
        self.options_button = pygame.Rect((self.width - self.button_width) / 2, self.start_button.bottom + self.button_spacing, self.button_width, self.button_height)
        self.quit_button = pygame.Rect((self.width - self.button_width) / 2, self.options_button.bottom + self.button_spacing, self.button_width, self.button_height)

        # Set up text animations
        self.title_text = self.title_font.render('Pykemon', True, (255, 255, 255))          #set up the variable to be used later
        self.title_animation_text = 200
        self.title_animation_check = True

    def run(self, screen):
        # Main loop
        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button.collidepoint(event.pos):
                        print('Start button clicked!')
                    elif self.options_button.collidepoint(event.pos):
                        print('Options button clicked!')
                        options_menu = PykemonOptionsMenu(self.width, self.height)
                        options_menu.run(screen)
                    elif self.quit_button.collidepoint(event.pos):
                        pygame.quit()
                        return

            # Draw background
            screen.blit(self.sky_color, (0, 0))
            # pygame.draw.rect(screen, self.grass_color, pygame.Rect(0, self.height - 200, self.width, 200))
            # pygame.draw.rect(screen, self.road_color, pygame.Rect(0, self.height - 100, self.width, 100))

            # Draw title
            title_rect = self.title_text.get_rect(center=(self.width / 2, self.title_animation_text))
            screen.blit(self.title_text, title_rect)

            # Draw buttons
            pygame.draw.rect(screen, (255, 255, 255), self.start_button)
            pygame.draw.rect(screen, (255, 255, 255), self.options_button)
            pygame.draw.rect(screen, (255, 255, 255), self.quit_button)

            # Update
            # Draw button text
            self.start_text = self.button_font.render('Start Game', True, (0, 0, 0))
            self.start_text_rect = self.start_text.get_rect(center=self.start_button.center)
            screen.blit(self.start_text, self.start_text_rect)

            self.options_text = self.button_font.render('Fake Options', True, (0, 0, 0))
            self.options_text_rect = self.options_text.get_rect(center=self.options_button.center)
            screen.blit(self.options_text, self.options_text_rect)

            self.quit_text = self.button_font.render('Quit', True, (0, 0, 0))
            self.quit_text_rect = self.quit_text.get_rect(center=self.quit_button.center)
            screen.blit(self.quit_text, self.quit_text_rect)

            # Update display
            pygame.display.flip()

