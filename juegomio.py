import pygame
import threading
import random
import time


pygame.init()

COLOR_FONDO = (10, 10, 30)
COLOR_METEORO = (255, 80, 80)
COLOR_JUGADOR = (80, 200, 255)

#tamaño de la ventana
ANCHO = 1280
ALTO = 720

#posicion inicial de la navesita
jugador_x = ANCHO / 2
jugador_y = ALTO - 100

#la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))

#creacion del reloj
reloj = pygame.time.Clock()
FPS = 60

juego_activo = True

meteoros = [] 




#Clase meteorito
class Meteoro(threading.Thread):
    def __init__(self):
        super().__init__()
        self.x = random.randint(0, ANCHO)
        self.y = -50
        self.velocidad = random.randint(3, 7)
        self.vivo = True

    def run(self):
        print("h")
        while self.vivo and juego_activo:
            self.y += self.velocidad

            if self.y > ALTO + 50:
                self.vivo = False  

            time.sleep(0.02) 

    def generador_meteoros():
        while juego_activo:
            nuevo = Meteoro()
            meteoros.append(nuevo)
            nuevo.start()  # inicia el hilo del meteoro

            time.sleep(0.7)  # cada cuanto se generan las piedras esas


# iniciar el generador de peñones
hilo_generador = threading.Thread(target=Meteoro.generador_meteoros)
hilo_generador.start()

#loop principal
while juego_activo:
    reloj.tick(FPS)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            juego_activo = False

    pantalla.fill(COLOR_FONDO)

    #dibujo de la nave
    pygame.draw.rect(   
        pantalla,
        COLOR_JUGADOR,        # color de la navesita
        (jugador_x, jugador_y, 50, 50)  # tamaño de la navesita
    )

    for m in meteoros:
        if m.vivo:
            pygame.draw.circle(pantalla, COLOR_METEORO, (int(m.x), int(m.y)), 20)

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        jugador_x -= 5

    if teclas[pygame.K_RIGHT]:
        jugador_x += 5


    pygame.display.flip() #Se muestra todo lo dibujado

pygame.quit
