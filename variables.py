import pygame

from Circle import Circle
from EventsHandler import EventsHandler
from ReflectingBall import ReflectingBall

size = [2000, 2000]
screen = pygame.display.set_mode(size)
box = pygame.Rect(0, 0, screen.get_width(), screen.get_width())
circle = Circle(screen.get_width() / 2, screen.get_height() / 2, screen.get_width() / 4)
Ball = ReflectingBall(screen)
Ball.speed = 10
Ball.angle = 45
event_handler = EventsHandler(Ball, circle, box)

__all__ = ['size', 'screen', 'box', 'circle', 'Ball', 'event_handler']
