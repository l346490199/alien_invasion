#!/bin/python3
#-*- coding: utf-8 -*-
# ship.py
# @author 刘秋
# @email lq@aqiu.info
# @description 飞船的类
# @created 2019-08-16T11:21:33.165Z+08:00
# @last-modified 2019-08-18T09:57:52.507Z+08:00
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

    def update(self):
        '''根据移动标识调整飞船位置-计算'''
        center = float(self.rect.centerx)
        botto = float(self.rect.bottom)
        if self.moving_right:
            center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            center -= self.ai_settings.ship_speed_factor
        if self.moving_down:
            botto += self.ai_settings.ship_speed_factor
        if self.moving_up:
            botto -= self.ai_settings.ship_speed_factor
        self.__get_update(botto, center)


    def __get_update(self, botto, center):
        ''' 修改位置条件'''
        if center > self.ai_settings.screen_width:
            center = 1
        if center < 0:
            center = self.ai_settings.screen_width - 1
        if botto > self.ai_settings.screen_height:
            botto = 1
        if botto < 0:
            botto = self.ai_settings.screen_height - 1
        self.rect.bottom = botto
        self.rect.centerx = center

    def blitme(self):
        '''在指定位置位置飞船'''
        self.screen.blit(self.image, self.rect)
