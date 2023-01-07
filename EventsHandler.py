import numpy as numpy
import pygame

from Circle import Circle
from ReflectingBall import ReflectingBall


class EventsHandler:
    def __init__(self, Ball, circle, box):
        self.not_exit_was_pressed = True
        self.Ball = Ball
        self.circle = circle
        self.box = box

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.not_exit_was_pressed = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.not_exit_was_pressed = False

        self.handle_Ball_events()

    def handle_Ball_events(self):
        # todo remove this
        self.Ball: ReflectingBall
        self.box: pygame.Rect
        self.circle: Circle
        #
        self.move_Ball()

        if self.Ball.pos[1] == 0:
            print("Ball cross top side")
        elif self.Ball.pos[1] == self.box.height:
            print("Ball cross bot side")

    # new_x = old_x + (speed * math.cos(angle_in_radians))
    # new_y = old_y + (speed * math.sin(angle_in_radians))
    def move_Ball(self):
        if self.Ball.angle == 0:
            self.Ball.pos[0] = self.Ball.pos[0] + self.Ball.speed
            self.Ball.pos[1] = self.Ball.pos[1] + self.Ball.speed * numpy.tan(self.Ball.angle)
            
        else:
            angle = numpy.radians(-self.Ball.angle)
            self.Ball.pos[0] = self.Ball.pos[0] + self.Ball.speed * numpy.cos(angle)
            self.Ball.pos[1] = self.Ball.pos[1] + self.Ball.speed * numpy.sin(angle)

        # self.Ball.end_pos[0] += self.Ball.speed
