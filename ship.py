#!/bin/python3
#-*- coding: utf-8 -*-
# ship.py
# @author 刘秋
# @email lq@aqiu.info
# @description 飞船的类
# @created 2019-08-16T11:21:33.165Z+08:00
# @last-modified 2019-08-16T11:37:27.061Z+08:00
#

import pygame

class Ship():
    '''飞船类'''
    def __init__(self, screen):
        '''初始化飞船 并设置其初始位置'''
        self.screen = screen

        # 加载飞船图像并获取其外形矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        '''在指定位置位置飞船'''
        self.screen.blit(self.image, self.rect)
        