import pygame
import time
pygame.init()
screen = pygame.display.set_mode((1000, 500))
x = 0 
y = 10
azul = [0,0,255]
rosa = [255,0,255]
# Dibuja un cuadrado en (x=100, y=100)
running = True
screen.fill((255, 255, 255))  # Blanco de fondo
while running:
    x += 8
    
    
    pygame.draw.rect(screen, rosa, (x, y, 32, 12))  
    pygame.draw.rect(screen,azul, (x-8, y+3, 8, 5))
    pygame.display.flip()
    time.sleep(0.1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
