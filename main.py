# Importamos el módulo random para seleccionar palabras aleatorias
import random

# Función que retorna una palabra aleatoria de una lista predefinida
def obtener_palabra():
    # Lista de posibles palabras para el juego
    palabras = ['python', 'programacion', 'computadora', 'desarrollo', 'tecnologia', 'videojuego']
    # Retorna una palabra aleatoria en minúsculas
    return random.choice(palabras).lower()

# Función que muestra el estado actual del juego
def mostrar_tablero(palabra_oculta, letras_incorrectas, intentos):
    # Limpia la pantalla imprimiendo líneas en blanco
    print("\n" * 50)  # Limpiar pantalla
    # Muestra el título del juego
    print("JUEGO DEL AHORCADO")
    print("==================")
    # Muestra los intentos restantes
    print(f"Te quedan {intentos} intentos")
    # Muestra la palabra oculta con espacios entre letras
    print("\nPalabra:", " ".join(palabra_oculta))
    # Muestra las letras incorrectas intentadas
    print("\nLetras incorrectas:", " ".join(letras_incorrectas))
    
# Función principal del juego
def jugar():
    # Obtiene la palabra aleatoria
    palabra = obtener_palabra()
    # Crea una lista de guiones bajos del mismo tamaño que la palabra
    palabra_oculta = ["_"] * len(palabra)
    # Inicializa la lista de letras incorrectas
    letras_incorrectas = []
    # Establece el número de intentos inicial
    intentos = 6
    
    # Bucle principal del juego mientras queden intentos
    while intentos > 0:
        # Muestra el estado actual del juego
        mostrar_tablero(palabra_oculta, letras_incorrectas, intentos)
        
        # Solicita una letra al jugador
        letra = input("\nIngresa una letra: ").lower()
        
        # Verifica que se ingrese una sola letra
        if len(letra) != 1:
            print("Por favor ingresa una sola letra")
            continue
        
        # Verifica si la letra está en la palabra
        if letra in palabra:
            # Si está, revela todas las ocurrencias de la letra
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    palabra_oculta[i] = letra
        else:
            # Si no está y no se había intentado antes, reduce intentos
            if letra not in letras_incorrectas:
                letras_incorrectas.append(letra)
                intentos -= 1
        
        # Verifica si se ha completado la palabra
        if "_" not in palabra_oculta:
            mostrar_tablero(palabra_oculta, letras_incorrectas, intentos)
            print("\n¡Felicidades! ¡Has ganado!")
            break
    
    # Si se agotan los intentos, muestra mensaje de derrota
    if intentos == 0:
        mostrar_tablero(palabra_oculta, letras_incorrectas, intentos)
        print("\n¡Game Over! La palabra era:", palabra)

# Bloque principal del programa
if __name__ == "__main__":
    # Bucle para permitir múltiples partidas
    while True:
        # Inicia una partida
        jugar()
        # Pregunta si se quiere jugar otra vez
        if input("\n¿Quieres jugar de nuevo? (s/n): ").lower() != 's':
            break
    
    # Mensaje de despedida
    print("\n¡Gracias por jugar!")




