#!/bin/python3
#-*- coding: utf-8 -*-
# game_functions.py
# @author 刘秋
# @email lq@aqiu.info
# @description 补充invasion
# @created 2019-08-16T11:47:13.765Z+08:00
# @last-modified 2019-08-19T13:35:26.678Z+08:00
#

import sys

import pygame

from alien import Alien
from bullet import Bullet


def check_events(ai_settings, screen, ship, bullets):
    '''响应按键和鼠标事件'''
    # 监视键盘和鼠标 事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #结束 关闭界面  参数 0   不写报错
            sys.exit(0)
        # 判断按键按下
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        # 判断 按键松开
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keyup_events(event, ship):
    ''' 当按键松开时'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False
    if event.key == pygame.K_q:
        sys.exit(0)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    '''当按键按下时'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    if event.key == pygame.K_SPACE:
        #按下空格生成一个子弹，并将其加入到编组bullets中
        fire_bullet(bullets, ai_settings, screen, ship)

def fire_bullet(bullets, ai_settings, screen, ship):
    ''' 如果还没有达到上限，就发射一颗子弹'''
    #按下空格生成一个子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    ''' 更新屏幕上的图像，并切换到新屏幕'''
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    #放置飞船
    ship.blitme()
    # 放置外星人
    aliens.draw(screen)
    #让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(bullets):
    ''' 更新子弹位置，并删除已消失的子弹'''
    # 子弹移动
    bullets.update()
    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            #print(len(bullets))

def create_fleet(ai_settings, screen, aliens):
    ''' 创建外星人群'''
    # 创建一个外星人，并计算一行可以容纳多少外星人
    # 外星人间距为外星人宽度
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)

    # 创建第一行外星人
    for alien_number in range(number_aliens_x):
        #创建一个外星人并将其加入当前行
        create_alien(ai_settings, screen, alien_number, aliens)

def get_number_aliens_x(ai_settings, alien_width):
    ''' 计算一行可以容纳多少外星人'''
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, alien_number, aliens):
    '''创建一个外星人并将其加入当前行'''
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)
