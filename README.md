# Juego de Naves con Meteoritos (Pygame)

Este proyecto es un minijuego creado en **Python** usando la librería
**Pygame**, donde controlas una nave que debe esquivar meteoritos que
caen desde la parte superior de la pantalla.

------------------------------------------------------------------------

##  Características del juego

-   La nave se mueve horizontalmente con las flechas **←** y **→**.
-   Los meteoritos se generan continuamente mediante hilos
    (`threading`).
-   Si un meteorito choca con la nave, el juego termina y aparece un
    mensaje de derrota.
-   El juego corre a **60 FPS**.

------------------------------------------------------------------------

##  Archivos necesarios

-   `main.py` → archivo principal del juego\
-   `README.md` → este archivo de documentación

------------------------------------------------------------------------

##  Cómo ejecutar el juego

1.  Asegúrate de tener **Python 3.8+** instalado.

2.  Instala Pygame:

    ``` bash
    pip install pygame
    ```

3.  Ejecuta el programa:

    ``` bash
    python main.py
    ```

------------------------------------------------------------------------

##  Explicación rápida del código

###  Jugador

Representado como un rectángulo azul que se mueve horizontalmente.

###  Meteoritos

Cada meteorito es un hilo independiente que cae hacia abajo con
velocidad aleatoria.

###  Colisiones

Se detectan usando `pygame.Rect` tanto para la nave como para el
meteoro.

