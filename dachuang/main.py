import graph.graph as gra
import pygame

pygame.init()
pygame.display.set_caption("My Board")
exit = False
start , end , idx , grid = gra.show_map()

print(start)
print(end)
print(idx)
print(grid)
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True