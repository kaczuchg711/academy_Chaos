import pygame

pygame.init()
size = [2000, 2000]
screen = pygame.display.set_mode(size)

not_exit_was_pressed = True

while not_exit_was_pressed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            not_exit_was_pressed = False
    circle_central_point = (screen.get_width() / 2, screen.get_height() / 2)
    pygame.draw.circle(screen, (255, 255, 255), circle_central_point, screen.get_width() / 4, 1)
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, screen.get_width(), screen.get_height()), width=1)
    pygame.display.flip()
