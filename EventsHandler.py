import pygame


class EventsHandler:
    def __init__(self):
        self.not_exit_was_pressed = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.not_exit_was_pressed = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.not_exit_was_pressed = False