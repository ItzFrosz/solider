import pygame

pygame.init()

# задаем размеры окна
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# задаем цвета
white = (255, 255, 255)
black = (0, 0, 0)

# задаем размеры и скорость квадрата
square_size = 50
square_speed = 0

# задаем начальную позицию квадрата
square_x = screen_width / 2 - square_size / 2
square_y = screen_height - square_size

# флаг для проверки, находится ли квадрат в воздухе
is_jumping = False

# функция для обработки событий
def handle_events():
    global square_speed, is_jumping
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                print("4434")
                square_speed += 10
            elif event.key == pygame.K_SPACE:
                if not is_jumping:
                    is_jumping = True
                    jump()

# функция для обновления состояния квадрата
def update_square():
    global square_x, square_y, is_jumping
    if is_jumping:
        square_y -= 15
        if square_y < screen_height - 2 * square_size:
            is_jumping = False
    else:
        square_y += square_speed
        if square_y > screen_height - square_size:
            square_y = screen_height - square_size

# функция для отрисовки квадрата
def draw_square():
    pygame.draw.rect(screen, white, (square_x, square_y, square_size, square_size))

# функция для реализации прыжка
def jump():
    global square_y, is_jumping
    for i in range(50):
        square_y -= 2
        if square_y < screen_height - 2 * square_size:
            is_jumping = False
            break
        update_screen()
        pygame.time.delay(10)

# функция для обновления экрана
def update_screen():
    screen.fill(black)
    draw_square()
    pygame.display.flip()

# главный игровой цикл
running = True
while running:
    # обработка событий
    handle_events()
    
    # обновление состояния квадрата
    update_square()
    
    # отрисовка квадрата
    update_screen()
    
    # проверка на выход из игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
