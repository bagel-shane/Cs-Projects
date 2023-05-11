import pygame
import os
from time import sleep


class ScareMenu:
    def __init__(self, screen_width, screen_height):

        # Set the Width and the Height
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Enviorment Variables

        # Background Colors
        self.background = (0,0,0) # sets the background color to Black

        # Set font and font size
        self.font = pygame.font.SysFont('Arial', 32)
        self.title_font = pygame.font.SysFont('Arial', 64)

         # Set up buttons
        self.button_width = 200
        self.button_height = 50
        self.button_spacing = 20

        # Set up buttons for design
        self.yes_button = pygame.Rect((self.screen_width - self.button_width) / 2, 400, self.button_width, self.button_height)
        self.no_button = pygame.Rect((self.screen_width - self.button_width) / 2, self.yes_button.bottom + self.button_spacing, self.button_width, self.button_height)

        self.yes_text = self.font.render('Yes', True, (0, 0, 0))
        self.yes_text_rect = self.yes_text.get_rect(center=self.yes_button.center)

        self.no_text = self.font.render('No', True, (0, 0, 0))
        self.no_text_rect = self.no_text.get_rect(center=self.no_button.center)



        # Scary Font
        self.text = 'You think this a game...'
        # Creation of the Scare Text
        self.title_text = self.title_font.render(self.text, True, (255, 255, 255))

    def run(self, screen):
        text_input = ""
        show_buttons = True
        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if show_buttons:
                        if self.yes_button.collidepoint(event.pos):
                            show_buttons = False
                        elif self.no_button.collidepoint(event.pos):
                            pygame.quit()
                            return

            # Set the background color
            screen.fill(self.background)

            if show_buttons:
                # Create the Title font
                title_rect = self.title_text.get_rect(center=(self.screen_width / 2, 200))
                screen.blit(self.title_text, title_rect)

                # Draw buttons and their text
                pygame.draw.rect(screen, (255, 255, 255), self.yes_button)
                pygame.draw.rect(screen, (255, 255, 255), self.no_button)
                screen.blit(self.yes_text, self.yes_text_rect)
                screen.blit(self.no_text, self.no_text_rect)

            else:
            # Creates a Scarier message to tell the user to leave it alone
                message_font = pygame.font.SysFont('Arial', 128)
                message_text1 = message_font.render('YOU', True, (255, 0, 0))
                message_text2 = message_font.render('ARE', True, (255, 0, 0))
                message_text3 = message_font.render('WRONG', True, (255, 0, 0))

                # Display the message so that there is a delay between words
                screen.blit(message_text1, (self.screen_width / 2 - message_text1.get_width() / 2, 200))
                pygame.display.flip()
                sleep(1)

                screen.blit(message_text2, (self.screen_width / 2 - message_text2.get_width() / 2, 400))
                pygame.display.flip()
                sleep(1)

                screen.blit(message_text3, (self.screen_width / 2 - message_text3.get_width() / 2, 600))
                pygame.display.flip()
                sleep(1)

                pygame.quit()
            # Update display
            pygame.display.flip()


