#!/bin/python3/n
# -*- coding: utf-8 -*-
# alien_invasion.py
# @author 刘秋
# @email lq@aqiu.info
# @description 开始的地方
# @created 2019-08-16T09:18:39.584Z+08:00
# @last-modified 2019-08-16T14:05:54.193Z+08:00
#

import pygame

import game_functions as gf
from settings import Settings
from ship import Ship


def run_game():
    ''' 游戏开始了'''
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 开始游戏的主循环
    while True:

        gf.check_events(ship)
        gf.update_screen(ai_settings, screen, ship)
        # 飞船移动
        ship.update()


run_game()
