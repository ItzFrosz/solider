import pygame

class Soldier(pygame.sprite.Sprite):

    #Переміщення вправо чи вліво
    moving_right = False
    moving_left = False

    speed = 1
    
    action = 0 # 0 - Стоїть, 1 - ходить, 2 - вмирає

    #Направлення переміщення
    flip = False
    direction = 1
    #Масив для списку анімацій
    animations_list = []
    #Кадр анімації
    frame_index = 0

    def __init__(self,x,y,scale,speed):
        pygame.sprite.Sprite.__init__(self)
        #scale - розмір спрайту(на випадок, що картинка маленька чи велика)
        self.scale = scale
        
        self.load_animation("idle",7)
        self.load_animation("walk",7)
        #Перша анімація - відпочинок, тобто 0
        self.action = 0
        self.image = self.animations_list[self.action][0]

        #rect - дійсне знаходження персонажу
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        #Підрахунок оновлення часу для оновлення кадру анімації
        self.update_time = pygame.time.get_ticks()

        self.speed = speed
        self.x = x
        self.y = y

    #Загружати нашу анімації
    def load_animation(self, name, length):
        temp_list = []
        for i in range(length):
            #Коротко : загружаємо, настройка розміру та встановлення кадру
            #для майбутньої анімації
            img = pygame.image.load(f"images/player/{name}/{i}.png")
            img = pygame.transform.scale(img,
                        (
                            int(img.get_width() * self.scale),
                            int(img.get_height() * self.scale)
                        ))
                        #Додання кадру в анімацію
            temp_list.append(img)
        #додаємо вже готову анімацію в список
        self.animations_list.append(temp_list)

    #Малюємо персонажа
    def draw(self,screen):
        screen.blit(pygame.transform.flip(self.animations_list[self.action][self.frame_index], self.flip, False), self.rect)
        #Переміщення
        self.move()
        #Оновлення анімації
        self.update_animation()
    #Переміщення
    def move(self):
        dx = 0
        dy = 0
        #Якщо йдемо, то й анімація буде ходьби, тобто 1
        if self.moving_left or self.moving_right:
            self.action = 1
        else :
            self.action = 0

        if self.moving_left:
            dx = -self.speed #Це потрібно для того, щоб змінювати нашу дійсну позицію
            self.direction = -1
            self.flip = True # True - наліво
        if self.moving_right:
            dx = self.speed # Поміть : - потрібно ставити у випадку, коли потрібно 
            self.direction = 1 # йти вліво, тобто в мінусову координату
            self.flip = False #False - направо
        #Зміна вже позиції ігрока під нові координати
        self.rect.x += dx
        self.rect.y += dy

    #Оновлення анімації
    def update_animation(self):
        #Частота оновлення
        ANIMATION_COOLDOWN = 100
        #Показ картинки нашого вже персонажу
        self.image = self.animations_list[self.action][self.frame_index]

        #Міняє з часом місце для нової картинки
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        #Перевірка чи анімація не зайде далі за кількість кадрів
        if self.frame_index >= len(self.animations_list[self.action]):
            self.frame_index = 0