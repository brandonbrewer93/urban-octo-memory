import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	
	def __init__(self, ai_settings, screen):
		"""Initialize the ship and set its starting position"""
		super(Ship, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		
		# Load the ship image and get its rect.
		self.image = pygame.image.load('images/new_ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		# Start each new ship at the bottom center of the screen.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		# Store a decimal value for the ship's center.
		self.center = float(self.rect.centerx)
		
		# Movement flags
		self.moving_right = False
		self.moving_left = False
		
		# Sounds
		self.ship_fire_sound = pygame.mixer.Sound('sounds/ship_gun.ogg')
		self.ship_fire_sound.set_volume(.1)
		
	def play_sound(self):
		self.ship_fire_sound.play()
		
	def update(self):
		"""Update the ship's position mased on the movement flag."""
		# Update the ships center valie
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left> 0:
			self.center -= self.ai_settings.ship_speed_factor
			
		# Update rect object from self.center.
		self.rect.centerx = self.center

		
		
	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)
		
	def center_ship(self):
		"""Center the ship on the screen."""
		self.center = self.screen_rect.centerx


