#!/bin/python3
#-*- coding: utf-8 -*-
# settings.py
# @author 刘秋
# @email lq@aqiu.info
# @description 参数设置
# @created 2019-08-16T10:14:09.086Z+08:00
# @last-modified 2019-08-18T09:50:11.161Z+08:00
#


class Settings():
    """"存储《外星人入侵》的所有设置的类 """
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 2
        #子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        