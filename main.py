import pygame

from EventsHandler import EventsHandler

pygame.init()
size = [2000, 2000]
screen = pygame.display.set_mode(size)

i = 0
event_handler = EventsHandler()

line_start_pos = [screen.get_width() * 0.9, screen.get_height() * 0.9]
line_end_pos = [screen.get_width() * 0.9, screen.get_height() * 0.8]

dx = - 2
while event_handler.not_exit_was_pressed:
    screen.fill((0, 0, 0))

    event_handler.handle_events()

    circle_central_point = (screen.get_width() / 2, screen.get_height() / 2)
    pygame.draw.circle(screen, (255, 255, 255), circle_central_point, screen.get_width() / 4, 1)
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, screen.get_width(), screen.get_height()), width=1)

    pygame.draw.line(screen, (255, 255, 255), line_start_pos,line_end_pos)
    if (line_end_pos[1] == 0):
        dx = 2
    line_start_pos[1] += dx
    line_end_pos[1] += dx

    pygame.display.flip()
