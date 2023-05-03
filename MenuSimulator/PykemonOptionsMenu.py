import pygame

class PykemonOptionsMenu:
    def __init__(self, screen_width, screen_height):
        # Set the Width and the Height
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Set colors
        self.sky_color = (135, 206, 235)  # Light blue sky
        self.grass_color = (124, 252, 0)  # Green grass
        self.road_color = (222, 184, 135)  # Light tan road

        # Set font and font size
        self.font = pygame.font.SysFont('Arial', 32)
        self.title_font = pygame.font.SysFont('Arial', 64)

        # Set up buttons
        self.button_width = 200
        self.button_height = 50
        self.button_spacing = 20

        self.volume_up_button = pygame.Rect((self.screen_width - self.button_width) / 2, 400, self.button_width, self.button_height)
        self.volume_down_button = pygame.Rect((self.screen_width - self.button_width) / 2, self.volume_up_button.bottom + self.button_spacing, self.button_width, self.button_height)
        self.back_button = pygame.Rect((self.screen_width - self.button_width) / 2, self.volume_down_button.bottom + self.button_spacing, self.button_width, self.button_height)

        # Set up text
        self.title_text = self.title_font.render('Options', True, (255, 255, 255))

        self.volume_up_text = self.font.render('Volume Up', True, (0, 0, 0))
        self.volume_up_text_rect = self.volume_up_text.get_rect(center=self.volume_up_button.center)

        self.volume_down_text = self.font.render('Volume Down', True, (0, 0, 0))
        self.volume_down_text_rect = self.volume_down_text.get_rect(center=self.volume_down_button.center)

        self.back_text = self.font.render('Back', True, (0, 0, 0))
        self.back_text_rect = self.back_text.get_rect(center=self.back_button.center)

    def run(self, screen):
        # Main loop
        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.volume_up_button.collidepoint(event.pos):
                        print('Volume Up button clicked!')
                        # Increase volume here
                    elif self.volume_down_button.collidepoint(event.pos):
                        print('Volume Down button clicked!')
                        # Decrease volume here
                    elif self.back_button.collidepoint(event.pos):
                        return

            # Draw background
            screen.fill(self.sky_color)
            pygame.draw.rect(screen, self.grass_color, pygame.Rect(0, self.screen_height - 200, self.screen_width, 200))
            pygame.draw.rect(screen, self.road_color, pygame.Rect(0, self.screen_height - 100, self.screen_width, 100))

            # Draw title
            title_rect = self.title_text.get_rect(center=(self.screen_width / 2, 200))
            screen.blit(self.title_text, title_rect)

            # Draw buttons
            pygame.draw.rect(screen, (255, 255, 255), self.volume_up_button)
            pygame.draw.rect(screen, (255, 255, 255), self.volume_down_button)
            pygame.draw.rect(screen, (255, 255, 255), self.back_button)

            # Draw button text
            screen.blit(self.volume_up_text, self.volume_up_text_rect)
            screen.blit(self.volume_down_text, self.volume_down_text_rect)
            screen.blit(self.back_text, self.back_text_rect)

            # Update display
            pygame.display.flip()
