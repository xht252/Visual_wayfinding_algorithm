import graph.graph as gra
import algorithm.algorithm as algorithm
import pygame

pygame.init()
pygame.display.set_caption("My Board")
exit = False
start , end , idx , grid , screen = gra.show_map()
algorithm.dfs(start , end , grid , screen)

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True