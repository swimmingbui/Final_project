import pygame

class BlackBall:
    def __init__(self, bi_game):
        self.screen = bi_game.screen
        self.screen_rect = bi_game.screen.get_rect()

        # Load the ball image and get its rect.
        self.image = pygame.image.load('images/Billiards/black_ball.png')
        self.image = pygame.transform.smoothscale(self.image, (40, 40))
        self.ball_rect = self.image.get_rect()

        #position for where the black ball spawns
        self.position = [400,200]

    def blitme(self):
        self.screen.blit(self.image, self.position)