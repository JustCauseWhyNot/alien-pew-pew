class GameStats:
	"""Stats!!!"""
	
	def __init__(self, ai_game):
		"""initalize stats"""
		self.settings = ai_game.settings
		self.reset_stats()
		
	def reset_stats(self):
		"""initalize dynamic stats"""
		self.ships_left = self.settings.ship_limit
		self.score = 0
