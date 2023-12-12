class Settings:
	""""Class for settings."""

	def __init__(self):
		"""Initalize settings"""
		
		self.screen_width = 800
		self.screen_height = 600
		self.bg_color = (13, 17, 23)

		self.ship_speed = 5

		self.bullet_speed = 2
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (255, 255, 0)
		self.bullets_allowed = 3
	
		"""Alien settings"""
		self.alien_speed = 1
		self.fleet_drop_speed = 10
		self.fleet_direction =1

