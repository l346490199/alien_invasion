#!/bin/python3/n
# -*- coding: utf-8 -*-
# alien_invasion.py
# @author 刘秋
# @email lq@aqiu.info
# @description 开始的地方
# @created 2019-08-16T09:18:39.584Z+08:00
# @last-modified 2019-08-16T11:54:18.936Z+08:00
#

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    ''' 游戏开始了'''
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(screen)
    # 开始游戏的主循环
    while True:

        gf.check_events()
        # 每次循环时都重绘屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        #让最近绘制的屏幕可见
        pygame.display.flip()


run_game()
