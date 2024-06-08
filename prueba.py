import pygame
import time
import random

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
window = pygame.display.set_mode((720, 480))
pygame.display.set_caption('Snake Game')

# Definición de colores
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Definición de velocidad del juego
snake_speed = 15

# Controlador de cuadros por segundo (FPS)
fps = pygame.time.Clock()

# Función para mostrar el puntaje
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Puntaje : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    window.blit(score_surface, score_rect)

# Función para el fin del juego
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Tu puntaje es : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (360, 15)
    window.blit(game_over_surface, game_over_rect)

    # Agregar opciones para reiniciar o salir
    replay_font = pygame.font.SysFont('times new roman', 30)

    # Presiona R para reiniciar o Q para salir del juego.
    replay_surface = replay_font.render('Presiona R para Reiniciar o Q para Salir.', True, white)
    replay_rect = replay_surface.get_rect()
    replay_rect.midtop = (360, 200)
    window.blit(replay_surface, replay_rect)

    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:  # Salir del juego
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_r:  # Reiniciar el juego
                    main()

# Función principal del juego
def main():
    global snake_speed
    global score

    # Posición inicial de la serpiente
    snake_pos = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50]]

    # Posición inicial de la fruta
    fruit_pos = [random.randrange(1, 72) * 10, random.randrange(1, 48) * 10]
    fruit_spawn = True

    # Configuración de dirección
    direction = 'RIGHT'
    change_to = direction

    # Puntuación inicial
    score = 0

    # Bucle principal del juego
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'

        # Si dos teclas presionadas al mismo tiempo
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Movimiento de la serpiente
        if direction == 'UP':
            snake_pos[1] -= 10
        if direction == 'DOWN':
            snake_pos[1] += 10
        if direction == 'LEFT':
            snake_pos[0] -= 10
        if direction == 'RIGHT':
            snake_pos[0] += 10

        # Cuerpo de la serpiente crece
        snake_body.insert(0, list(snake_pos))

        # Si la serpiente come la fruta
        if snake_pos[0] == fruit_pos[0] and snake_pos[1] == fruit_pos[1]:
            fruit_spawn = False
            score += 1
            snake_speed += 1
        else:
            snake_body.pop()

        # Si la fruta fue comida
        if not fruit_spawn:
            fruit_pos = [random.randrange(1, 72) * 10, random.randrange(1, 48) * 10]
        fruit_spawn = True

        # Limpiar la pantalla
        window.fill(black)

        # Dibujar la serpiente
        for pos in snake_body:
            pygame.draw.rect(window, green, pygame.Rect(pos[0], pos[1], 10, 10))

        # Dibujar la fruta
        pygame.draw.rect(window, white, pygame.Rect(fruit_pos[0], fruit_pos[1], 10, 10))

        # Mostrar el puntaje
        show_score(1, white, 'times new roman', 20)

        # Condiciones para perder el juego
        if snake_pos[0] < 0 or snake_pos[0] > 720-10:
            game_over()
        if snake_pos[1] < 0 or snake_pos[1] > 480-10:
            game_over()

        for block in snake_body[1:]:
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                game_over()

        # Actualizar la pantalla
        pygame.display.update()
        fps.tick(snake_speed)

# Llamar a la función principal del juego
main()