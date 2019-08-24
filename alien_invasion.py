#!/bin/python3
# -*- coding: utf-8 -*-
"""
# alien_invasion.py
# @author 刘秋
# @email lq@aqiu.info
# @description 开始的地方
# @created 2019-08-16T09:18:39.584Z+08:00
# @last-modified 2019-08-23T11:03:07.854Z+08:00
#"""

import pygame
from pygame.sprite import Group

import game_functions as gf
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard
from settings import Settings
from ship import Ship


def run_game():
    """ 游戏开始了"""
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    # 实例一个设置参数
    ai_settings = Settings()
    # 窗口屏幕
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    # 屏幕名称
    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮实例
    play_button = Button(ai_settings, screen, "play")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个子弹组
    bullets = Group()
    # 创建一群外星人实例
    aliens = Group()
    gf.create_fleet(ai_settings, screen, aliens, ship)
    # 创建一个用于存储游戏统计信息的实例,并创建得分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # 开始游戏的主循环
    while True:

        gf.check_events(ai_settings, screen, ship, bullets, stats, play_button, aliens)
        if stats.game_active:
            # 飞船移动
            ship.update()
            gf.update_bullets(bullets, aliens, ai_settings, screen, ship)
            gf.update_aliens(aliens, ai_settings, ship, bullets, screen, stats)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets, stats, play_button, sb)


if __name__ == '__main__':
    run_game()
