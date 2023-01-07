import pygame

from Circle import Circle
from EventsHandler import EventsHandler
from ReflectingBall import ReflectingBall
from variables import *


def draw_circle(screen, circle):
    pygame.draw.circle(screen, circle.color, (circle.x, circle.y), circle.radius, circle.boarder_width)


def main():
    clock = pygame.time.Clock()
    pygame.init()


    while event_handler.not_exit_was_pressed:
        screen.fill((0, 0, 0))

        event_handler.handle_events()
        draw_circle(screen, circle)
        pygame.draw.rect(screen, (255, 255, 255), box, width=1)
        pygame.draw.circle(screen, event_handler.Ball.color, event_handler.Ball.pos, 50)

        pygame.display.flip()
        clock.tick(60)
        screen.blit(pygame.transform.flip(screen, True, False), (0, 0))

if __name__ == '__main__':
    main()
