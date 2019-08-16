#!/bin/python3
#-*- coding: utf-8 -*-
# ship.py
# @author 刘秋
# @email lq@aqiu.info
# @description 飞船的类
# @created 2019-08-16T11:21:33.165Z+08:00
# @last-modified 2019-08-16T16:21:30.539Z+08:00
#

import pygame


class Ship():
    '''飞船类'''
    def __init__(self, ai_settings, screen):
        '''初始化飞船 并设置其初始位置'''
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外形矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)
        self.botto = float(self.rect.bottom)

    def update(self):
        '''根据移动标识调整飞船位置-计算'''
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_down:
            self.botto += self.ai_settings.ship_speed_factor
        if self.moving_up:
            self.botto -= self.ai_settings.ship_speed_factor
        self.__get_update()
        self.rect.bottom = self.botto
        self.rect.centerx = self.center

    def __get_update(self):
        ''' 修改位置条件'''
        if self.center > self.ai_settings.screen_width:
            self.center = 1
        if self.center < 0:
            self.center = self.ai_settings.screen_width - 1
        if self.botto > self.ai_settings.screen_height:
            self.botto = 1
        if self.botto < 0:
            self.botto = self.ai_settings.screen_height - 1

    def blitme(self):
        '''在指定位置位置飞船'''
        self.screen.blit(self.image, self.rect)
