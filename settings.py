class Settings:
	""""Class for settings."""

	def __init__(self):
		"""Initalize settings"""
		
		self.screen_width = 800
		self.screen_height = 600
		self.bg_color = (13, 17, 23)

		self.ship_speed = 5
		self.ship_limit = 3

		self.bullet_speed = 2
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (255, 255, 0)
		self.bullets_allowed = 3
	
		"""Alien settings"""
		self.alien_speed = 1
		self.fleet_drop_speed = 10
		self.fleet_direction = 1
		self.speedup_scale = 2
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Initalize dynamic settings"""
		self.ship_speed = 10
		self.bullet_speed = 2.5
		self.alien_speed = 1.0
		self.fleet_direction = 1

	def increase_speed(self):
		"""increase speed settings"""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale
