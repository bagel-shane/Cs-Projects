import pygame
import os
from PykemonMenu import PykemonMenu

class MenuSimulator:
    def __init__(self, width, height):
        # Starting up pygame window
        pygame.init()

        # Set the Width and the Height
        self.width = width
        self.height = height

        # Background Colors
        self.sky_color = pygame.image.load(os.path.join('MenuSimulator/Assets', 'This_Is_a_Game.png')) # Light blue sky

        # Set font size for buttons and for the Title Text
        self.button_font = pygame.font.SysFont('Arial', 32)
        self.title_font = pygame.font.SysFont('calibri', 96)
        # Set window title

        # Create Menu screen
        self.screen = pygame.display.set_mode((self.width, self.height))

        # Set up buttons
        self.button_width = 200
        self.button_height = 50
        self.button_spacing = 20

        self.start_button = pygame.Rect((self.width - self.button_width) / 2, 400, self.button_width, self.button_height)
        self.quit_button = pygame.Rect((self.width - self.button_width) / 2, self.start_button.bottom + self.button_spacing, self.button_width, self.button_height)

        # Set up text animations
        self.title_text = self.title_font.render('This Is Not a Game', True, (255, 255, 255))          #set up the variable to be used later
        self.title_animation_text = 200
        self.title_animation_check = True

    def run(self):
        # Main loop
        while True:
            # Handling the change in events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button.collidepoint(event.pos):
                        new_menu = PykemonMenu(self.width, self.height)
                        new_menu.run(self.screen)

                    elif self.quit_button.collidepoint(event.pos):
                        pygame.quit()
                        return

            # Drawing background image
            self.screen.blit(self.sky_color, (0, 0))

            # Draw title sequence
            title_rect = self.title_text.get_rect(center=(self.width / 2, self.title_animation_text))
            if 150 <= self.title_animation_text <= 200 and self.title_animation_check == True: #goes up
                self.title_animation_text = self.title_animation_text - 0.05

            elif self.title_animation_text < 150:                                      
                self.title_animation_text = self.title_animation_text + 0.05
                self.title_animation_check = False

            elif 150 <= self.title_animation_text <= 200 and self.title_animation_check == False: 
                self.title_animation_text = self.title_animation_text + 0.05
                
            elif self.title_animation_text > 200:
                self.title_animation_text = self.title_animation_text - 0.05
                self.title_animation_check = True
                
            self.screen.blit(self.title_text, title_rect)

            # Draw buttons on the screen
            pygame.draw.rect(self.screen, (255, 255, 255), self.start_button)
            pygame.draw.rect(self.screen, (255, 255, 255), self.quit_button)

            # Drawing the  button text
            self.start_text = self.button_font.render('Start Game', True, (0, 0, 0))
            self.start_text_rect = self.start_text.get_rect(center=self.start_button.center)
            self.screen.blit(self.start_text, self.start_text_rect)

            self.quit_text = self.button_font.render('Quit', True, (0, 0, 0))
            self.quit_text_rect = self.quit_text.get_rect(center=self.quit_button.center)
            self.screen.blit(self.quit_text, self.quit_text_rect)

            # Update display
            pygame.display.flip()

            

