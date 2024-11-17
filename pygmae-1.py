# Dibujar líneas, rectángulos y círculos en la ventana del juego
import pygame, sys
from colores import *

pygame.init()

dimension = (700, 500) # Dimensiones de la ventana (ancho, alto)

# Ventana del juego
pantalla = pygame.display.set_mode(dimension)

while True:
    for event in pygame.event.get(): # Eventos del juego
        if event.type == pygame.QUIT: # Si se cierra la ventana
            quit() # Salir del juego
            sys.exit() # Salir del programa

    # Define el color de fondo de la ventana
    pantalla.fill(BLANCO)

    # -------- CODIGO PARA DIBUJAR AQUI --------

    # Dibujar linea (explicar cómo se trabaja con el eje X y Y)
    punto_inicio = (20, 20) # (X, Y)
    punto_fin = (350, 20) # (X, Y)
    pygame.draw.line(pantalla, ROJO, punto_inicio, punto_fin, 5) # (linea, color, punto inicial, punto final, grosor)

    # Dibujar rectángulo
    ancho = 100
    alto = 100
    pygame.draw.rect(pantalla, VERDE, (20, 50, ancho, alto)) # (ventana, color, (X, Y, ancho, alto))

    # Dibujar círculo
    radio = 50
    #pygame.draw.circle(pantalla, AZUL, (20, 180), radio) # (ventana, color, (X, Y), radio)
    pygame.draw.circle(pantalla, AZUL, (70, 230), radio) # (ventana, color, (X, Y), radio)

    # La documentación de Pygame se encuentra en: https://www.pygame.org/docs/ o buscando pygame.draw en Google

    # -------- FIN DEL CÓDIGO DE DIBUJO --------
    # Actualiza la ventana
    pygame.display.update()