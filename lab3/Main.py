import pygame
from pygame.draw import *

pygame.init()

FPS = 30
sc = pygame.display.set_mode((685, 969))
pi = 3.14

rect(sc, (255, 255, 255), (0, 0, 685, 969), 0)
rect(sc, (220, 220, 220), (0, 0, 685, 400), 0)
ellipse(sc, (220, 220, 220), (70, 370, 320, 300))
rect(sc, (255, 255, 255), (70, 520, 320, 200), 0)   # clear
arc(sc, (0, 0, 0), (70, 370, 320, 300), 0, pi, 4)
line(sc, (0, 0, 0), [70, 510], [390, 510], 4)
line(sc, (0, 0, 0), [82, 460], [378, 460], 2)
line(sc, (0, 0, 0), [125, 410], [335, 410], 2)
ellipse(sc, (220, 220, 220), (500, 500, 130, 100))   # head
ellipse(sc, (110, 90, 90), (490, 550, 150, 250))   # body
ellipse(sc, (148, 126, 126), (515, 515, 100, 70))   # head
ellipse(sc, (220, 220, 220), (530, 535, 70, 40))
line(sc, (0, 0, 0), [547, 547], [557, 553], 2)
line(sc, (0, 0, 0), [587, 547], [574, 553], 2)
arc(sc, (0, 0, 0), (555, 564, 20, 10), 0, pi, 2)
rect(sc, (255, 255, 255), (490, 690, 320, 200), 0)   # clear
ellipse(sc, (110, 90, 90), (450, 590, 80, 30))   # body
ellipse(sc, (110, 90, 90), (600, 590, 80, 30))
ellipse(sc, (110, 90, 90), (510, 660, 40, 70))
ellipse(sc, (110, 90, 90), (580, 660, 40, 70))
ellipse(sc, (110, 90, 90), (497, 710, 50, 25))
ellipse(sc, (110, 90, 90), (585, 710, 50, 25))
rect(sc, (59, 42, 42), (548, 583, 35, 91))
rect(sc, (59, 42, 42), (490, 675, 150, 16))
line(sc, (0, 0, 0), [460, 500], [460, 740], 1)
ellipse(sc, (220, 220, 220), (120, 740, 150, 40))   # cat
ellipse(sc, (220, 220, 220), (110, 710, 50, 40))
polygon(sc, (220, 220, 220), ([[120, 715], [130, 700], [132, 712]]))
polygon(sc, (220, 220, 220), ([[138, 711], [155, 701], [155, 725]]))
ellipse(sc, (220, 220, 220), (60, 755, 90, 20))
ellipse(sc, (220, 220, 220), (70, 775, 90, 20))
ellipse(sc, (220, 220, 220), (210, 775, 90, 20))
ellipse(sc, (220, 220, 220), (240, 755, 90, 20))
ellipse(sc, (220, 220, 220), (245, 735, 110, 30))
ellipse(sc, (255, 255, 255), (113, 720, 14, 13))
ellipse(sc, (255, 255, 255), (133, 723, 14, 13))
ellipse(sc, (0, 0, 0), (120, 720, 9, 7))
ellipse(sc, (0, 0, 0), (140, 723, 9, 7))
polygon(sc, (0, 0, 0), ([[122, 737], [128, 739], [122, 745]]))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()