import pygame
import sys
from time import sleep
from lib_tron import colision
# Inicialización
pygame.init()
ANCHO, ALTO = 400, 500
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Botella con fuga")

# Parámetros de la botella
x, y = 150, 100
ancho_botella = 100
alto_botella = 300
nivel = alto_botella  # Nivel inicial (lleno)
vel_vaciado = 5
vel_llenado = 1

# Control del estado
esperando = False
tiempo_vacio = 0

# Colores
VERDE = (0, 255, 0)
NEGRO = (0, 0, 0)
GRIS = (200, 200, 200)

reloj = pygame.time.Clock()
def main():
    global nivel
    ya_vacio = False
    while True:
        presionando = pygame.mouse.get_pressed()[0]
        # Cálculo del color del líquido
        porcentaje = 1 - (nivel / alto_botella)
        r = int((1 - porcentaje) * 0   + porcentaje * 255)
        g = int((1 - porcentaje) * 255 + porcentaje * 0)
        porcentaje_vacio = 1 - (nivel / alto_botella)
        r = int(porcentaje_vacio * 255)
        g = int((1 - porcentaje_vacio) * 255)
        color_liquido = (r, g, 0)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Si está vacío, iniciar el conteo si no ha comenzado
        if nivel < 0 and not ya_vacio:
            nivel = 0
            ya_vacio = True  # evitamos repetir
            sleep(1)
            print("1")
            sleep(1)
            print("2")
            sleep(1)
            print("3")
            print(ya_vacio)
            
                
        else:
            if ya_vacio:
                presionando = False
                ya_vacio = False
            
            if presionando:
                if nivel >= 0:
                    nivel -= vel_vaciado
            else:
                if nivel < alto_botella:
                    nivel += vel_llenado
        
        # Dibujo
        pantalla.fill(GRIS)

        # Dibuja la botella (solo el borde)
        pygame.draw.rect(pantalla, NEGRO, (x, y, ancho_botella, alto_botella), 3)

        # Dibuja el líquido verde
        altura_liquido = nivel
        try:
            pygame.draw.rect(pantalla, color_liquido, (x + 3, y + alto_botella - altura_liquido + 3, ancho_botella - 6, altura_liquido - 6))
        except ValueError:
            pass
        pygame.display.flip()
        reloj.tick(60)
main()