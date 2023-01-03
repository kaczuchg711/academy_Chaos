import pygame

from EventsHandler import EventsHandler
from ReflectingLine import ReflectingLine

pygame.init()
size = [2000, 2000]
screen = pygame.display.set_mode(size)

i = 0
event_handler = EventsHandler()

line = ReflectingLine(screen)
line.speed = - 2





while event_handler.not_exit_was_pressed:
    screen.fill((0, 0, 0))

    event_handler.handle_events()

    circle_central_point = (screen.get_width() / 2, screen.get_height() / 2)
    pygame.draw.circle(screen, (255, 255, 255), circle_central_point, screen.get_width() / 4, 1)
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, screen.get_width(), screen.get_height()), width=1)

    pygame.draw.line(screen, line.color, line.start_pos, line.end_pos)

    # todo change direction if line touch smt
    if line.end_pos[1] == 0:
        line.speed = 2

    line.start_pos[1] += line.speed
    line.end_pos[1] += line.speed

    pygame.display.flip()
