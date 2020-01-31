import sys

import pygame

from bullet import Bullet
from alien import Alien


def check_events(ai_settings, screen, ship, bullets):
    """响应事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(ai_settings, screen, event, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(ai_settings, screen, event, ship, bullets):
    """响应按键"""
    # 开始向右移动飞船
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    # 开始向左移动飞船
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    # 创建子弹并加入子弹编组
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    # 按Q退出游戏
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """响应按键松开"""
    # 停止向右移动飞船
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    # 停止向左移动飞船
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """更新屏幕图像"""
    screen.fill(ai_settings.bg_color)
    # 绘制子弹编组中的子弹
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blit_me()
    aliens.draw(screen)

    pygame.display.flip()


def update_bullets(bullets):
    """更新子弹位置，删除消失子弹"""
    # 更新子弹位置
    bullets.update()

    # 删除已消失子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    """发射子弹"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(ai_settings, screen, aliens):
    """创建外星人群"""
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    for alien_number in range(number_aliens_x):
        create_alien(ai_settings, screen, aliens, number_aliens_x)


def get_number_aliens_x(ai_settings, alien_width):
    """计算每行可容纳多少外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    num_aliens_x = int(available_space_x / (2 * alien_width))
    return num_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number):
    """创建一个外星人"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)
