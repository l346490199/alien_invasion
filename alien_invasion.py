#!/bin/python3/n
# -*- coding: utf-8 -*-
# alien_invasion.py
# @author 刘秋
# @email lq@aqiu.info
# @description da
# @created 2019-08-16T09:18:39.584Z+08:00
# @last-modified 2019-08-16T11:06:32.045Z+08:00
#

import sys
import pygame
from settings import Settings


def run_game():
    ''' 游戏开始了'''
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 开始游戏的主循环
    while True:

        # 监视键盘和鼠标 事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #结束 关闭界面  参数 0   不写报错
                sys.exit(0)
        # 每次循环时都重绘屏幕
        screen.fill(ai_settings.bg_color)
        #让最近绘制的屏幕可见
        pygame.display.flip()


run_game()
