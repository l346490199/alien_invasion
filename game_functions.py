#!/bin/python3
#-*- coding: utf-8 -*-
# game_functions.py
# @author 刘秋
# @email lq@aqiu.info
# @description 补充invasion
# @created 2019-08-16T11:47:13.765Z+08:00
# @last-modified 2019-08-16T14:06:23.110Z+08:00
#

import sys
import pygame


def check_events(ship):
    '''响应按键和鼠标事件'''
    # 监视键盘和鼠标 事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #结束 关闭界面  参数 0   不写报错
            sys.exit(0)
        # 判断按键按下
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                ship.moving_left = True
            if event.key == pygame.K_UP:
                ship.moving_up = True
            if event.key == pygame.K_DOWN:
                ship.moving_down = True
        # 判断 按键松开
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False
            if event.key == pygame.K_UP:
                ship.moving_up = False
            if event.key == pygame.K_DOWN:
                ship.moving_down = False

def update_screen(ai_settings, screen, ship):
    ''' 更新屏幕上的图像，并切换到新屏幕'''
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    #放置飞船
    ship.blitme()
    #让最近绘制的屏幕可见
    pygame.display.flip()
