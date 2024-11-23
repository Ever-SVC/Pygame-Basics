# Mover un rectángulo en la ventana del juego con las teclas de dirección
import pygame, sys
from colores import *

pygame.init()

dimension = (700, 500) # Dimensiones de la ventana (ancho, alto)
# ----
# Coordenadas iniciales del rectángulo
cord_x = 20
cord_y = 50

# Velocidad de movimiento del rectángulo
velocidad = 5

# Reloj del juego (para controlar la velocidad de actualización de la ventana Frame Per Second)
reloj = pygame.time.Clock()
# ----

# Ventana del juego
ventana = pygame.display.set_mode(dimension)

while True:
    for event in pygame.event.get(): # Eventos del juego
        if event.type == pygame.QUIT: # Si se cierra la ventana
            quit() # Salir del juego
            sys.exit() # Salir del programa

        # Eventos de teclado para mover el rectángulo (Buscar pygame.key en Google)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                cord_x -= velocidad
            if event.key == pygame.K_RIGHT:
                cord_x += velocidad
            if event.key == pygame.K_UP:
                cord_y -= velocidad
            if event.key == pygame.K_DOWN:
                cord_y += velocidad
    
    # Evita que el rectángulo salga de la ventana
    if cord_x < 0: # Si la coordenada X es menor a 0
        cord_x = 0 # La coordenada X es 0
    if cord_x > dimension[0] - 100: # Si la coordenada X es mayor al ancho de la ventana - 100 (ancho del rectángulo)
        cord_x = dimension[0] - 100 # La coordenada X es igual al ancho de la ventana - 100 (ancho del rectángulo)
    if cord_y < 0:
        cord_y = 0
    if cord_y > dimension[1] - 100:
        cord_y = dimension[1] - 100


    # Define el color de fondo de la ventana
    ventana.fill(BLANCO)

    # -------- CÓDIGO PARA DIBUJAR AQUI --------

    # Dibujar rectángulo
    ancho = 100
    alto = 100
    pygame.draw.rect(ventana, VERDE, (cord_x, cord_y, ancho, alto)) # (ventana, color, (X, Y, ancho, alto))

    # -------- FIN DEL CÓDIGO DE DIBUJO --------

    # Actualiza la ventana
    pygame.display.update()
    reloj.tick(60) # 60 FPS