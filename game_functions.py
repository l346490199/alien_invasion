#!/bin/python3
# -*- coding: utf-8 -*-
"""# game_functions.py
# @author 刘秋
# @email lq@aqiu.info
# @description 补充invasion
# @created 2019-08-16T11:47:13.765Z+08:00
# @last-modified 2019-08-23T11:01:32.498Z+08:00
#"""

import sys
from time import sleep

import pygame

from alien import Alien
from bullet import Bullet


def check_events(ai_settings, screen, ship, bullets, stats, play_button, aliens):
    """
    响应按键和鼠标事件
    """
    # 监视键盘和鼠标 事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 结束 关闭界面  参数 0   不写报错
            sys.exit(0)
        # 判断按键按下
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        # 判断 按键松开
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship, ai_settings, aliens, bullets, screen, stats)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y, aliens, bullets, ai_settings, screen, ship)


def check_play_button(stats, play_button, mouse_x, mouse_y, aliens, bullets, ai_settings, screen, ship):
    """
    在玩家单机Play按钮时开始游戏
    """
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # 隐藏鼠标
        pygame.mouse.set_visible(False)
        # 重新开始游戏
        start_game(ai_settings, aliens, bullets, screen, ship, stats)


def start_game(ai_settings, aliens, bullets, screen, ship, stats):
    """

    启动游戏
    """
    # 重置游戏设置
    ai_settings.initialize_dynamic_settings()
    # 重置游戏统计信息
    stats.reset_stats()
    stats.game_active = True
    # 清空外星人列表和子弹列表
    aliens.empty()
    bullets.empty()
    # 创建一群新的外星人，并让飞船居中
    create_fleet(ai_settings, screen, aliens, ship)


def check_keyup_events(event, ship, ai_settings, aliens, bullets, screen, stats):
    """
    当按键松开时
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False
    if event.key == pygame.K_q:
        sys.exit(0)
    if event.key == pygame.K_t and not stats.game_active:
        start_game(ai_settings, aliens, bullets, screen, ship, stats)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """当按键按下时"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    if event.key == pygame.K_SPACE:
        # 按下空格生成一个子弹，并将其加入到编组bullets中
        fire_bullet(bullets, ai_settings, screen, ship)


def fire_bullet(bullets, ai_settings, screen, ship):
    """ 如果还没有达到上限，就发射一颗子弹"""
    # 按下空格生成一个子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_screen(ai_settings, screen, ship, aliens, bullets, stats, play_button, sb):
    """ 更新屏幕上的图像，并切换到新屏幕  """
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 放置飞船
    ship.blitme()
    # 放置外星人
    aliens.draw(screen)
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 显示得分
    sb.show_score()
    # 如果游戏处在非活动状态，就显示Play按钮
    if not stats.game_active:
        play_button.draw_button()
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(bullets, aliens, ai_settings, screen, ship, stats, sb):
    """ 更新子弹位置，并删除已消失的子弹    """
    # 子弹移动
    bullets.update()
    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            # print(len(bullets))
    # 子弹和外星人碰撞
    check_bullet_alien_collisions(bullets, aliens, ai_settings, screen, ship, stats, sb)


def check_high_score(stats, sb):
    """检查是否诞生了新的最高分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def check_bullet_alien_collisions(bullets, aliens, ai_settings, screen, ship, stats, sb):
    """ 响应子弹和外星人的碰撞
    """
    # 删除发生碰撞的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            # 消灭外星人 得分加分
            stats.score += ai_settings.alien_points * len(aliens)
            # 得分牌 刷新
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # 删除现有的子弹并新建一群外星人
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, aliens, ship)


def create_fleet(ai_settings, screen, aliens, ship):
    """ 创建外星人群"""
    # 创建一个外星人，并计算一行可以容纳多少外星人
    # 外星人间距为外星人宽度
    alien = Alien(ai_settings, screen)
    # 计算一行多少个alien
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    # 计算有多少列 alien
    number_rows = get_number_rows(ai_settings, ship.rect.height,
                                  alien.rect.height)

    for row_number in range(number_rows):
        # 创建第一行外星人
        for alien_number in range(number_aliens_x):
            # 创建一个外星人并将其加入当前行
            create_alien(ai_settings, screen, alien_number, aliens, row_number)


def get_number_aliens_x(ai_settings, alien_width):
    """ 计算一行可以容纳多少外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, alien_number, aliens, row_number):
    """创建一个外星人并将其加入当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    # 改横坐标
    alien.rect.x = alien.x
    # 改纵坐标
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_rows(ai_settings, ship_height, alien_height):
    """ 计算屏幕可以容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) -
                         ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def update_aliens(aliens, ai_settings, ship, bullets, screen, stats):
    """ 更新外星人群中所有外星人位置"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(aliens, ai_settings, ship, bullets, screen, stats)
    # 检查外星人是否到达屏幕底部
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)


def ship_hit(aliens, ai_settings, ship, bullets, screen, stats):
    """ 响应被外星人撞到的飞船"""
    if stats.ships_left > 0:
        # 将ship_left减一
        stats.ships_left -= 1

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并将飞船放到屏幕底端中央
        create_fleet(ai_settings, screen, aliens, ship)
        ship.center_ship()

        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_fleet_edges(ai_settings, aliens):
    """ 有外星人到达边缘时采取相应措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """ 外星人向下移动，变换方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """ 检查外星人是否到达屏幕底部"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞击一样处理
            ship_hit(aliens, ai_settings, ship, bullets, screen, stats)
            break
