import random
import pygame #libreria para poner el juego en 2d
import os

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
ANCHO = 800
ALTO = 600
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego del Ahorcado 2D")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (128, 128, 128)

# Configuración de fuentes
FUENTE_GRANDE = pygame.font.Font(None, 48)
FUENTE_PEQUEÑA = pygame.font.Font(None, 36)

# Palabras para el juego
def obtener_palabra():
    palabras = ['python', 'programacion', 'computadora', 'desarrollo', 'tecnologia', 'videojuego']
    return random.choice(palabras).lower()
# ... existing code for obtener_palabra() ...

def dibujar_ahorcado(intentos):
    # Dibuja el poste
    pygame.draw.line(PANTALLA, NEGRO, (100, 500), (300, 500), 5)  # base
    pygame.draw.line(PANTALLA, NEGRO, (200, 500), (200, 100), 5)  # poste vertical
    pygame.draw.line(PANTALLA, NEGRO, (200, 100), (400, 100), 5)  # poste horizontal
    pygame.draw.line(PANTALLA, NEGRO, (400, 100), (400, 150), 5)  # cuerda

    if intentos < 6:  # cabeza
        pygame.draw.circle(PANTALLA, NEGRO, (400, 180), 30, 5)
    if intentos < 5:  # cuerpo
        pygame.draw.line(PANTALLA, NEGRO, (400, 210), (400, 350), 5)
    if intentos < 4:  # brazo izquierdo
        pygame.draw.line(PANTALLA, NEGRO, (400, 250), (340, 300), 5)
    if intentos < 3:  # brazo derecho
        pygame.draw.line(PANTALLA, NEGRO, (400, 250), (460, 300), 5)
    if intentos < 2:  # pierna izquierda
        pygame.draw.line(PANTALLA, NEGRO, (400, 350), (340, 420), 5)
    if intentos < 1:  # pierna derecha
        pygame.draw.line(PANTALLA, NEGRO, (400, 350), (460, 420), 5)

def jugar():
    palabra = obtener_palabra()
    palabra_oculta = ["_"] * len(palabra)
    letras_incorrectas = []
    intentos = 6
    juego_terminado = False
    mensaje = ""
    
    while True:
        PANTALLA.fill(BLANCO)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
            if evento.type == pygame.KEYDOWN:
                if not juego_terminado:
                    if evento.key >= pygame.K_a and evento.key <= pygame.K_z:
                        letra = chr(evento.key)
                        if letra not in letras_incorrectas and letra not in palabra_oculta:
                            if letra in palabra:
                                for i in range(len(palabra)):
                                    if palabra[i] == letra:
                                        palabra_oculta[i] = letra
                            else:
                                letras_incorrectas.append(letra)
                                intentos -= 1
                else:
                    # Si el juego terminó, verifica si presionó S o N
                    if evento.key == pygame.K_s:
                        return True  # Volver a jugar
                    elif evento.key == pygame.K_n:
                        return False  # Terminar el juego

        # Dibujar elementos del juego
        dibujar_ahorcado(intentos)
        
        # Mostrar palabra oculta
        texto_palabra = FUENTE_GRANDE.render(" ".join(palabra_oculta), True, NEGRO)
        PANTALLA.blit(texto_palabra, (ANCHO//2 - texto_palabra.get_width()//2, 450))
        
        # Mostrar letras incorrectas
        texto_incorrectas = FUENTE_PEQUEÑA.render("Letras incorrectas: " + " ".join(letras_incorrectas), True, GRIS)
        PANTALLA.blit(texto_incorrectas, (20, 20))
        
        # Verificar victoria o derrota
        if not juego_terminado:
            if "_" not in palabra_oculta:
                mensaje = "¡Felicidades! ¡Has ganado!"
                juego_terminado = True
            elif intentos == 0:
                mensaje = f"¡Game Over! La palabra era: {palabra}"
                juego_terminado = True
            
        if juego_terminado:
            texto_final = FUENTE_GRANDE.render(mensaje, True, NEGRO)
            PANTALLA.blit(texto_final, (ANCHO//2 - texto_final.get_width()//2, 250))
            
            texto_reiniciar = FUENTE_PEQUEÑA.render("¿Quieres jugar de nuevo? (S/N)", True, GRIS)
            PANTALLA.blit(texto_reiniciar, (ANCHO//2 - texto_reiniciar.get_width()//2, 300))
        
        pygame.display.flip()
    
    return False

def main():
    jugando = True
    while jugando:
        jugando = jugar()
    
    pygame.quit()

if __name__ == "__main__":
    main()