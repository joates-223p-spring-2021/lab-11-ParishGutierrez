# -*- coding: utf-8 -*-
"""
Created on Mon May  2 18:39:15 2022

@author: paris
"""


class Settings:
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        
        # Ship settings
        self.ship_speed = 1
        
        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3