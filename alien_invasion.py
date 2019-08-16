#!/bin/python3/n
''' dd '''
# -*- coding: utf-8 -*-
# alien_invasion.py
# @author 刘秋
# @email lq@aqiu.info
# @description da
# @created 2019-08-16T09:18:39.584Z+08:00
# @last-modified 2019-08-16T11:01:54.033Z+08:00
#

import sys
import pygame


def run_game():
    ''' 游戏开始了'''
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    # 设置颜色
    bg_color = (230, 230, 230)

    # 开始游戏的主循环
    while True:

        # 监视键盘和鼠标 事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #结束 关闭界面  参数 0   不写报错
                sys.exit(0)
        # 每次循环时都重绘屏幕
        screen.fill(bg_color)
        #让最近绘制的屏幕可见
        pygame.display.flip()


run_game()
