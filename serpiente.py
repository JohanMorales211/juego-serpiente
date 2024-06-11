import pygame
import time
import random

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
window_width = 720
window_height = 480
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game')

# Colores
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
yellow = pygame.Color(255, 255, 0)

# Fuente del juego
font_style = 'times new roman'

# Velocidad del juego
snake_speed = 15

# Controlador de cuadros por segundo (FPS)
fps = pygame.time.Clock()

# Función para mostrar texto en pantalla
def mostrar_texto(texto, tamaño, color, x, y):
    font = pygame.font.SysFont(font_style, tamaño)
    texto_surface = font.render(texto, True, color)
    texto_rect = texto_surface.get_rect()
    texto_rect.center = (x, y)
    window.blit(texto_surface, texto_rect)

# Función para mostrar el puntaje
def mostrar_puntaje(puntaje):
    mostrar_texto("Puntaje: " + str(puntaje), 20, white, 60, 10)

# Función para el fin del juego
def game_over(puntaje):
    while True:
        window.fill(black)
        mostrar_texto("¡Game Over!", 50, red, window_width / 2, window_height / 4)
        mostrar_texto("Tu puntaje fue: " + str(puntaje), 30, white, window_width / 2, window_height / 2)
        mostrar_texto("Presiona R para reiniciar o Q para salir", 20, white, window_width / 2, window_height * 3 / 4)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_r:
                    main()

# Función para la pantalla de inicio
def pantalla_inicio():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Iniciar el juego al presionar espacio
                    return
        
        window.fill(black)
        mostrar_texto("Snake Game", 60, green, window_width / 2, window_height / 3)
        mostrar_texto("Por: Johan Morales", 20, white, window_width / 2, window_height / 3 + 70) # Nombre del autor
        mostrar_texto("Presiona Espacio para comenzar", 20, white, window_width / 2, window_height * 2 / 3)
        pygame.display.flip()

# Función principal del juego
def main():
    global snake_speed

    # Posición inicial de la serpiente
    snake_block_size = 10
    snake_speed = 15
    snake_x = window_width / 2
    snake_y = window_height / 2
    snake_x_change = 0
    snake_y_change = 0
    snake_list = []
    snake_length = 1

    # Posición inicial de la fruta
    fruit_block_size = 10
    fruit_x = round(random.randrange(0, window_width - fruit_block_size) / 10.0) * 10.0
    fruit_y = round(random.randrange(0, window_height - fruit_block_size) / 10.0) * 10.0

    # Dirección inicial aleatoria
    direcciones_posibles = ["derecha", "izquierda", "arriba", "abajo"]
    direccion_actual = random.choice(direcciones_posibles)

    # Mostrar la pantalla de inicio al iniciar el juego
    pantalla_inicio()

    # Bucle principal del juego
    game_over_flag = False
    while not game_over_flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over_flag = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direccion_actual != "derecha":
                    snake_x_change = -snake_block_size
                    snake_y_change = 0
                    direccion_actual = "izquierda"
                elif event.key == pygame.K_RIGHT and direccion_actual != "izquierda":
                    snake_x_change = snake_block_size
                    snake_y_change = 0
                    direccion_actual = "derecha"
                elif event.key == pygame.K_UP and direccion_actual != "abajo":
                    snake_y_change = -snake_block_size
                    snake_x_change = 0
                    direccion_actual = "arriba"
                elif event.key == pygame.K_DOWN and direccion_actual != "arriba":
                    snake_y_change = snake_block_size
                    snake_x_change = 0
                    direccion_actual = "abajo"

        # Mantener la serpiente dentro de los límites de la ventana
        if snake_x >= window_width or snake_x < 0 or snake_y >= window_height or snake_y < 0:
            game_over(snake_length - 1)

        snake_x += snake_x_change
        snake_y += snake_y_change
        window.fill(black)

        # Dibujar la fruta
        pygame.draw.rect(window, red, [fruit_x, fruit_y, fruit_block_size, fruit_block_size])

        # Lógica de la serpiente
        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_list.append(snake_head)

        # Ajustar la longitud de la serpiente
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Verificar si la serpiente choca consigo misma
        for x in snake_list[:-1]:
            if x == snake_head:
                game_over(snake_length - 1)

        # Dibujar la serpiente
        for x in snake_list:
            pygame.draw.rect(window, green, [x[0], x[1], snake_block_size, snake_block_size])

        # Verificar si la serpiente come la fruta
        if snake_x == fruit_x and snake_y == fruit_y:
            fruit_x = round(random.randrange(0, window_width - fruit_block_size) / 10.0) * 10.0
            fruit_y = round(random.randrange(0, window_height - fruit_block_size) / 10.0) * 10.0
            snake_length += 1

        mostrar_puntaje(snake_length - 1)
        pygame.display.update()
        fps.tick(snake_speed)

    pygame.quit()
    quit()

# Iniciar el juego
main() 