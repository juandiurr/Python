from lib_tron import Coordenates, colision, hht
import pygame
import sys
import random
import time

ANCHO, ALTO = 640, 480
ANCHO_MOTO, ALTO_MOTO = 12, 35
corriendo = 1

COLISION = True
CONS = 3

VER = False
VER_LINEAS = False
VER_PUNTOS = False

V_NORMAL = 6
V_TURBO = V_NORMAL*2
cooldown = True
velocidad = V_NORMAL
EVENTO_BOOST = pygame.USEREVENT + 1
EVENTO_COOLDOWN = pygame.USEREVENT + 2



ancho_moto = ANCHO_MOTO
alto_moto = ALTO_MOTO
DIFF = ALTO_MOTO - ANCHO_MOTO 
# Colores
COLOR = (255,0,255)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (49,255,109)
AMARILLO = (255,255,0)
AZUL = (0,0,255)
NEGRO = (0,0,0)
MORADO = (189,0,255)
NARANJA = (255,99,5)
ROSADO = (255,0,190)
AZUL_OSUCRO = (10,20,105)
MORADO_OSCURO = (115,13,200)
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pausa = False
vertical = {}
horizontal = {}
coords = Coordenates()
def cuadrado(color):
    pygame.draw.rect(pantalla, color, (0, 0, 15, 15))
def posicion(n):
    global x, y, derecha, izquierda, arriba, abajo, ancho_moto, alto_moto
    global coords
    if n == 1:
        x = 0
        y = 20
        derecha = 2
        izquierda = 0
        arriba = 0
        abajo = 0
        ancho_moto = ANCHO_MOTO
        alto_moto = ALTO_MOTO
        coords.append_c([x,y])
        coords.append_c([x,y+ANCHO_MOTO])
    if n == 2:
        x = ANCHO - ALTO_MOTO
        y = 20
        derecha = 0
        izquierda = 2
        arriba = 0
        abajo = 0
        ancho_moto = ANCHO_MOTO
        alto_moto = ALTO_MOTO
        coords.append_c([x+ALTO_MOTO,y])
        coords.append_c([x+ALTO_MOTO,y+ANCHO_MOTO])
    if n == 3:
        x = ANCHO - ALTO_MOTO
        y = 450
        derecha = 0
        izquierda = 2
        arriba = 0
        abajo = 0
        ancho_moto = ANCHO_MOTO
        alto_moto = ALTO_MOTO
        coords.append_c([x+ALTO_MOTO,y])
        coords.append_c([x+ALTO_MOTO,y+ANCHO_MOTO])
    if n == 4:
        x = 0
        y = 450
        derecha = 2
        izquierda = 0
        arriba = 0
        abajo = 0
        ancho_moto = ANCHO_MOTO
        alto_moto = ALTO_MOTO
        coords.append_c([x,y])
        coords.append_c([x,y+ANCHO_MOTO])
def ver():
    if VER:
        print("------------------------------------------")
        print("arriba: ", arriba) 
        print("abajo: ", abajo)  
        print("izquierda: ", izquierda)
        print("derecha: ", derecha)
        print("------------------------------------------")
def ver_lineas():
    if VER_LINEAS:
        for xx, segmentos in vertical.items():
            for y1, y2 in segmentos:
                pygame.draw.line(pantalla, (0,255,0),(xx,y1),(xx,y2),2)
        for yy, segmentos in horizontal.items():
            for x1, x2 in segmentos:
                pygame.draw.line(pantalla, (0,255,0),(x1,yy),(x2,yy),2)
    if VER_PUNTOS:
        for p in coords.ret():
            pygame.draw.circle(pantalla, (0,0,0), p, 2)
def eventos():
    global corriendo, derecha, izquierda, arriba, abajo, velocidad, x, y, ancho_moto, alto_moto #int
    global cooldown, pausa #boolean
    global vertical, horizontal #dict
    global coords #Coordenates
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = 255
        if evento.type == pygame.KEYDOWN:
            
            if evento.key == pygame.K_w:#ARRIBA
                if abajo != 2 and arriba != 2:
                    pygame.draw.rect(pantalla, COLOR, (x, y, ALTO_MOTO, ANCHO_MOTO))
                    ancho_moto = ALTO_MOTO
                    alto_moto = ANCHO_MOTO
                    derecha = hht(derecha)
                    izquierda = hht(izquierda)
                    arriba = 2
                    abajo = 0
                    if derecha == 1:
                        coords.append_c([x + DIFF, y])
                        pygame.time.delay(10)  
                        coords.append_c([x+ALTO_MOTO, y+ANCHO_MOTO])
                        y = y - DIFF
                        x = x + DIFF
                        
                    if izquierda == 1:
                        coords.append_c([x,y+ANCHO_MOTO])
                        pygame.time.delay(10)
                        coords.append_c([x+ANCHO_MOTO,y])
                        y = y - DIFF

                    ver()
            elif evento.key == pygame.K_a:#IZQUIERDA
                if derecha != 2 and izquierda != 2:
                    pygame.draw.rect(pantalla, COLOR, (x, y, ANCHO_MOTO, ALTO_MOTO))
                    ancho_moto = ANCHO_MOTO
                    alto_moto = ALTO_MOTO
                    derecha = 0
                    izquierda = 2
                    arriba = hht(arriba)
                    abajo = hht(abajo)
                    if abajo == 1:
                        coords.append_c([x,y+DIFF])
                        pygame.time.delay(10)
                        coords.append_c([x+ANCHO_MOTO,y+ALTO_MOTO])
                        y = y + DIFF 
                        x = x - DIFF

                    if arriba == 1:
                        coords.append_c([x+ANCHO_MOTO,y])
                        pygame.time.delay(10)
                        coords.append_c([x,y+ANCHO_MOTO])
                        x = x - DIFF

                    ver()
            elif evento.key == pygame.K_s:#ABAJO
                if arriba != 2 and abajo != 2:
                    pygame.draw.rect(pantalla, COLOR, (x, y, ALTO_MOTO, ANCHO_MOTO))
                    ancho_moto = ALTO_MOTO
                    alto_moto = ANCHO_MOTO
                    derecha = hht(derecha)
                    izquierda = hht(izquierda)
                    arriba = 0
                    abajo = 2
                    if derecha == 1:
                        coords.append_c([x+ALTO_MOTO,y])
                        pygame.time.delay(10)
                        coords.append_c([x+DIFF,y+ANCHO_MOTO])
                        x = x + DIFF

                    if izquierda == 1:
                        coords.append_c([x,y])
                        pygame.time.delay(10)
                        coords.append_c([x+ANCHO_MOTO,y+ANCHO_MOTO])

                    ver()
            elif evento.key == pygame.K_d:#DERECHA
                if izquierda != 2 and derecha != 2:
                    pygame.draw.rect(pantalla, COLOR, (x, y, ANCHO_MOTO, ALTO_MOTO))
                    ancho_moto = ANCHO_MOTO
                    alto_moto = ALTO_MOTO
                    derecha = 2
                    izquierda = 0
                    arriba = hht(arriba)
                    abajo = hht(abajo)
                    if abajo == 1:
                        coords.append_c([x,y+ALTO_MOTO])
                        pygame.time.delay(10)
                        coords.append_c([x+ANCHO_MOTO,y+DIFF])
                        y = y + DIFF

                    if arriba == 1:
                        coords.append_c([x,y])
                        pygame.time.delay(10)
                        coords.append_c([x+ANCHO_MOTO,y+ANCHO_MOTO])
                    ver()
                
            elif evento.key == pygame.K_e:
                corriendo = 255
            elif evento.key == pygame.K_f:
                if cooldown == True and velocidad != V_TURBO:
                    pygame.time.set_timer(EVENTO_BOOST, 3000)
                    velocidad = V_TURBO
                    cooldown = False
                    print("VELOCIDAD")
                else:
                    print("Boost en carga...")
            elif evento.key == pygame.K_r:
                if pausa:
                    pausa = False
                    
                else:
                    print()
                    print("Coords: ",coords)
                    
                    print("Verticales: ")
                    print(vertical)
                    print("Horizontales: ")
                    print(horizontal)
                    pausa = True
            if evento.key != pygame.K_f and evento.key != pygame.K_e and evento.key != pygame.K_r:
                
                
                vertical = vertical | coords.vertical()
                horizontal = horizontal | coords.horizontal()
                
                
                coords.keep_last()
                
         # Detectar click con el mouse
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:  # 1 = botón izquierdo
                if cooldown == True and velocidad != V_TURBO:
                    pygame.time.set_timer(EVENTO_BOOST, 3000)
                    velocidad = V_TURBO
                    cooldown = False
                    print("VELOCIDAD")
                else:
                    print("Boost en carga...")
            elif evento.button == 3:  # 3 = botón derecho
                print("Click derecho en:", evento.pos)
        if evento.type == EVENTO_BOOST:
            print("¡3 segundos han pasado!")
            velocidad = V_NORMAL
            
            pygame.time.set_timer(EVENTO_BOOST, 0)  # Desactiva el temporizador
            pygame.time.set_timer(EVENTO_COOLDOWN, 5000)
        if evento.type == EVENTO_COOLDOWN:
            print("Boost listo para usarse")
            pygame.time.set_timer(EVENTO_COOLDOWN, 0)
            cooldown = True
def start():
    global cooldown, velocidad
    SEP = random.randint(25,50)
    POSICION = random.randint(1,4)
    pantalla.fill(AZUL_OSUCRO)  # Pintar fondo blanco
    # Dibujar líneas verticales cada 5 píxeles
    for x in range(0, ANCHO, SEP):
        pygame.draw.line(pantalla, MORADO_OSCURO, (x, 0), (x, ALTO))

    # Dibujar líneas horizontales cada 5 píxeles
    for y in range(0, ALTO, SEP):
        pygame.draw.line(pantalla, MORADO_OSCURO, (0, y), (ANCHO, y))
    coords.clear()
    vertical.clear()
    horizontal.clear()
    cooldown = True
    velocidad = V_NORMAL
    pygame.time.set_timer(EVENTO_COOLDOWN, 0)
    pygame.time.set_timer(EVENTO_BOOST, 0)
    posicion(POSICION)
def fin_del_juego():
    pygame.draw.rect(pantalla, ROJO, (x, y, alto_moto, ancho_moto))
    pygame.display.flip()  
    time.sleep(2)
    start()
def main():
    FPS = 60
    pygame.init()
    global x
    global y
    #Define un evento personalizado
    global pausa
    global vertical, horizontal
    global coords
    # Crear una ventana
    
    
    pygame.display.set_caption("Mi primer juego")
    
    
    reloj = pygame.time.Clock()
    
    start()
    # Bucle principal
    
    
    while corriendo == 1:
        #Establecer FPS a 60
        ver_lineas()
        reloj.tick()  
        pygame.time.delay(60)  # pausa por 20 milisegundos
        eventos()
        
        while (pausa):
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_r:
                        pausa = False
                    elif evento.key == pygame.K_e:
                        pygame.quit()
                        sys.exit()
                    elif evento.key == pygame.K_f:
                        pausa = False
                        start()
        if derecha == 2:
            
            x = x + velocidad
            if x > ANCHO:
                x = 0 - ALTO_MOTO
                coords.append_c([ANCHO,y])
                coords.append_c([ANCHO,y+ANCHO_MOTO])
                vertical = vertical | coords.vertical()
                horizontal = horizontal | coords.horizontal()
                coords.clear()
                coords.append_c([x,y])
                coords.append_c([x,y+ANCHO_MOTO])
            pygame.draw.rect(pantalla, COLOR, (x-velocidad, y, velocidad, ANCHO_MOTO))
            for linea_x, seg in list(vertical.items()):
                for y1, y2 in seg:
                    if colision(y1, y2, y) or colision(y1, y2, y + ANCHO_MOTO):
                        if colision(x+ALTO_MOTO,x+ALTO_MOTO-DIFF,linea_x):  # rango vertical del jugador
                            fin_del_juego()
        if izquierda == 2:
            x = x - velocidad
            if x < 0 - ALTO_MOTO:
                x = ANCHO
                coords.append_c([0,y])
                coords.append_c([0,y+ANCHO_MOTO])
                vertical = vertical | coords.vertical()
                horizontal = horizontal | coords.horizontal()
                coords.clear()
                coords.append_c([x,y])
                coords.append_c([x,y+ANCHO_MOTO])
            pygame.draw.rect(pantalla, COLOR, (x+ALTO_MOTO, y, velocidad, ANCHO_MOTO))
            for linea_x, seg in list(vertical.items()):
                for y1, y2 in seg:
                    if colision(y1, y2, y) or colision(y1, y2, y + ANCHO_MOTO):
                        if colision(x,x+DIFF,linea_x):  # rango vertical del jugador
                            fin_del_juego()
        if arriba == 2:
            y = y - velocidad
            if y < 0 - ALTO_MOTO:
                y = ALTO
                coords.append_c([x,0])
                coords.append_c([x+ANCHO_MOTO,0])
                vertical = vertical | coords.vertical()
                horizontal = horizontal | coords.horizontal()
                coords.clear()
                coords.append_c([x,y+ALTO_MOTO])
                coords.append_c([x+ANCHO_MOTO,y+ANCHO_MOTO])
            pygame.draw.rect(pantalla, COLOR, (x, y+ALTO_MOTO, ANCHO_MOTO, velocidad))
            for linea_y, seg in list(horizontal.items()):
                for x1, x2 in seg:
                    if colision(x1, x2, x) or colision(x1, x2, x + ANCHO_MOTO):
                        if colision(y,y+DIFF,linea_y):  # rango vertical del jugador
                            fin_del_juego()
        if abajo == 2:
            y = y + velocidad
            if y > ALTO:
                y = 0 - ALTO_MOTO
                coords.append_c([x,ALTO])
                coords.append_c([x+ANCHO_MOTO,ALTO])
                vertical = vertical | coords.vertical()
                horizontal = horizontal | coords.horizontal()
                coords.clear()
                coords.append_c([x,y+ALTO_MOTO])
                coords.append_c([x+ANCHO_MOTO,y+ANCHO_MOTO])
            pygame.draw.rect(pantalla, COLOR, (x, y-velocidad, ANCHO_MOTO, velocidad))
            for linea_y, seg in list(horizontal.items()):
                for x1, x2 in seg:
                    if colision(x1, x2, x) or colision(x1, x2, x + ANCHO_MOTO):
                        if colision(y+ALTO_MOTO,y+ALTO_MOTO-DIFF,linea_y):  # rango vertical del jugador
                            fin_del_juego()
        pygame.draw.rect(pantalla, ROJO, (x, y, alto_moto, ancho_moto))  # Dibujar un cuadrado rojo

        pygame.display.flip()  # Actualizar la pantalla
    while corriendo == 2:
        pantalla.fill(BLANCO)  # Pintar fondo blanco
    if corriendo == 255:
        
        pygame.quit()
        sys.exit()
    # Salir del juego
    

if __name__ == "__main__":
    main()