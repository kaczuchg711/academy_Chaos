import pygame


class ReflectingLine:
    def __init__(self, screen):
        self.start_pos = [screen.get_width() * 0.9, screen.get_height() * 0.9]
        self.end_pos = [screen.get_width() * 0.9, screen.get_height() * 0.8]
        self.color = (255, 255, 255)
        self.speed = -2