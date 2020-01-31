import pygame


class Ship:
	
	def __init__(self, ai_settings, screen):
		""" 初始化飞船 """
		self.screen = screen
		self.ai_settings = ai_settings
		
		# 加载飞船图像，获取外接矩形
		self.image = pygame.image.load('images/rocket_0.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		# 将新飞船放在屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# 存储位置小数值
		self.center = float(self.rect.centerx)

		# 移动标识
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""根据移动标识调整飞船位置"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor

		self.rect.centerx = self.center

	def blit_me(self):
		# 绘制飞船
		self.screen.blit(self.image, self.rect)
