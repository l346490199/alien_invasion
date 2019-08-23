#!/bin/python3
# -*- coding: utf-8 -*-
'''
# settings.py
# @author 刘秋
# @email lq@aqiu.info
# @description 参数设置
# @created 2019-08-16T10:14:09.086Z+08:00
# @last-modified 2019-08-23T10:58:28.257Z+08:00
'''


class Settings():
    """"存储《外星人入侵》的所有设置的类 """

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 子弹设置
        self.bullet_width = 3000
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        # 子弹数量
        self.bullet_allowed = 3
        # 飞船的生命
        self.ship_limit = 3
        # 外星人下降距离
        self.fleet_drop_speed = 10

        self.initialize_dynamic_settings()
        self.speedup_scale = 1.1

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        # fleet_direction 为1表示向右移动，为-1 表示向左移动
        self.fleet_direction = 1
        # 外星人移动速度
        self.alien_speed_factor = 1
        # 子弹速度
        self.bullet_speed_factor = 3
        # 飞船速度
        self.ship_speed_factor = 2

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.fleet_direction *= self.speedup_scale
