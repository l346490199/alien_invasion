#!/bin/python3
#-*- coding: utf-8 -*-
'''
# game_stats.py
# @author 刘秋
# @email lq@aqiu.info
# @description 
# @created 2019-08-23T10:23:14.744Z+08:00
# @last-modified 2019-08-23T10:27:03.280Z+08:00
#'''

class GameStats():
    """" 跟踪游戏的统计数据"""
    def __init__ (self, ai_setting):
        ''' 初始化统计数据'''
        self.ai_setting = ai_setting
        self.reset_stats()
    
    def reset_stats(self):
        ''' 初始化在游戏运行期间可能变化的统计信息'''
        self.ships_left = self.ai_setting.ship_limit
