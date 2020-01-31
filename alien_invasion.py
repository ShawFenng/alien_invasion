import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
	# 配置初始化
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption(ai_settings.caption)
	
	# 飞船初始化
	ship = Ship(ai_settings, screen)
	# 创建子弹编组
	bullets = Group()
	# 创建外星人编组
	aliens = Group()
	gf.create_fleet(ai_settings, screen, aliens)

	# 游戏主循环
	while True:
		# 响应事件
		gf.check_events(ai_settings, screen, ship, bullets)
		# 更新飞船
		ship.update()
		# 更新子弹
		gf.update_bullets(bullets)
		# 更新屏幕
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
