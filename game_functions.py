#!/bin/python3
#-*- coding: utf-8 -*-
# game_functions.py
# @author 刘秋
# @email lq@aqiu.info
# @description 补充invasion
# @created 2019-08-16T11:47:13.765Z+08:00
# @last-modified 2019-08-16T11:51:17.051Z+08:00
#

import sys
import pygame


def check_events():
    '''响应按键和鼠标事件'''
    # 监视键盘和鼠标 事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #结束 关闭界面  参数 0   不写报错
            sys.exit(0)
