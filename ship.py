import pygame

class Ship:
	""""Class for ship."""

	def __init__(self, ai_game):
		""""Initalize ship."""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
	
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		
		self.rect.midbottom = self.screen_rect.midbottom
	
	def blitme(self):
		""""Draw ship."""
		self.screen.blit(self.image, self.rect)
