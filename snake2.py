import pygame
import time
import random

pygame.init()

# Определение цветов
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)

# Размеры игрового поля
dis_width = 800
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))

clock = pygame.time.Clock()

snake_block = 10
initial_speed = 4

font_style = pygame.font.SysFont(None, 35)

# Функция для отображения счета в левом верхнем углу экрана
def show_score(score):
    value = font_style.render("Очки: " + str(score), True, red)
    dis.blit(value, [0, 0])

# Функция для отрисовки змейки
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

# Функция для вывода сообщения
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    score = 0  # Начальный счет

    while not game_over:

        while game_close:
            dis.fill(white)
            message("Вы проиграли! Нажмите C-Играть или Q-Выйти", red)
            show_score(score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #завершение игрового цикла
                game_over = True
            if event.type == pygame.KEYDOWN: #проверка нажатия клавишь
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0: #проверка столкновения с границами
            game_close = True
        x1 += x1_change     #отрисовка змеи
        y1 += y1_change
        dis.fill(white)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block]) # появление еды
        snake_head = []
        snake_head.append(x1)        #добавление новой позиции головы
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:        #
            del snake_list[0]

        for x in snake_list[:-1]:          #проверка столкновения с собой
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        show_score(score)                   # Отображение текущего счета
        pygame.display.update()

        if x1 == foodx and y1 == foody:         #съедание еды и генерирование нового случайного места
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
            score += 1  # Увеличение счета

        snake_speed = initial_speed + (score // 5) * 2  # Изменение скорости змейки
        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
