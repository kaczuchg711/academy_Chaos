import pygame


class ReflectingBall:
    def __init__(self, screen, speed=1, angle=0, radius = 50):
        self.pos = [screen.get_width() * 0.2, screen.get_height() * 0.8]
        self.color = (255, 255, 255)
        self.speed = speed
        self.angle = angle
        self.radius = radius
