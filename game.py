import pygame
import random

screen_width = 1920
screen_hight = 1080

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_hight))
done = False

number_of_stars = 10000
speed = 2
stars = []

def new_star() -> list:
    return [
        random.randint(-screen_width // 2, screen_width // 2),
        random.randint(-screen_hight // 2, screen_hight // 2),
        256,
        random.randint(150, 255),
    ]

def move_and_check(star: list) -> list:
    star[2] -= speed
    if star[2] <= 0:
        return new_star()
    star[3] = min(255, star[3] + 0.3)
    return star

def draw_star(star: list) -> None:
    x = int((star[0] / star[2]) * screen_width + screen_width // 2)
    y = int((star[1] / star[2]) * screen_hight + screen_hight // 2)
    pygame.draw.circle(screen, (star[3], star[3], star[3]), (x, y), 3)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0, 0, 0))

    if len(stars) < number_of_stars:
        stars.append(new_star())

    for i in range(len(stars)):
        stars[i] = move_and_check(stars[i])
        draw_star(stars[i])

    pygame.display.flip()

pygame.quit()
