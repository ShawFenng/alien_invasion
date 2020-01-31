import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """外星人"""

    def __init__(self, ai_settings, screen):
        """初始化外星人"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载图像
        self.image = pygame.image.load('images/ufo_0.png')
        self.rect = self.image.get_rect()

        # 初始化位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储准确位置
        self.x = float(self.rect.x)

    def blit_me(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)