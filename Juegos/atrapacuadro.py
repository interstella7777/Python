import pygame #importo la libreria de Pygame
import random

# Inicializo la libreria Pygame
pygame.init()

# Configuración de la pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Atrapa el cuadrado Creado por Bryan Vivas") #Titulo de la ventana

# Colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

# Variables del jugador
jugador = pygame.Rect(ANCHO // 2, ALTO // 2, 50, 50)
velocidad = 5

# Variables del objetivo
objetivo = pygame.Rect(random.randint(0, ANCHO - 50), random.randint(0, ALTO - 50), 50, 50)

# Reloj para controlar FPS
reloj = pygame.time.Clock()

# Bucle principal del juego
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Movimiento del jugador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_UP] and jugador.top > 0:
        jugador.y -= velocidad
    if teclas[pygame.K_DOWN] and jugador.bottom < ALTO:
        jugador.y += velocidad
    if teclas[pygame.K_LEFT] and jugador.left > 0:
        jugador.x -= velocidad
    if teclas[pygame.K_RIGHT] and jugador.right < ANCHO:
        jugador.x += velocidad

    # Comprobar colisión con el objetivo
    if jugador.colliderect(objetivo):
        objetivo.x = random.randint(0, ANCHO - 50)
        objetivo.y = random.randint(0, ALTO - 50)

    # Dibujar en pantalla
    pantalla.fill(BLANCO)
    pygame.draw.rect(pantalla, AZUL, jugador)
    pygame.draw.rect(pantalla, ROJO, objetivo)
    pygame.display.flip()

    # Controlar FPS
    reloj.tick(30)

pygame.quit()
