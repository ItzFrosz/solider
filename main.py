import pygame
from soldier import Soldier

pygame.init()
#Розміри екрану
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
#Іконка для гри
ICON = pygame.image.load("icon.jpg")
#Встановлена значень для додатку
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#Вибір назви для гри
pygame.display.set_caption("ToasterGame")
#Вибір іконки для гри
pygame.display.set_icon(ICON)

#Ставимо замок для того, щоб була стабілізація 
#наших анімацій й швидкості оновлення екрану
FPS = 60
clock = pygame.time.Clock()

#Колір фону
BG = (71, 6, 201)
#Малювання фону
def draw_bg():
    screen.fill(BG)


#Змінна для підтримки життя гри
run = True

#Наш ігрок
player = Soldier(200,200,2.5,4)

while run:
    clock.tick(FPS)

    #Для очищення екрану, то малюємо заново фон
    draw_bg()

    #Малюємо ігрока
    player.draw(screen)

    #Натискання на кнопки
    for event in pygame.event.get():
        #Натискання крестику для закінчення гри
        if event.type == pygame.QUIT:
            run = False

        #Натискання кнопки на кв.
        if event.type == pygame.KEYDOWN:
            #Йти вліво
            if event.key == pygame.K_a:
                player.moving_left = True

            #Йти вправо
            if event.key == pygame.K_d:
                player.moving_right = True
            #Вихід з гри
            if event.key == pygame.K_ESCAPE:
                run = False
                break

        #Відпускання кнопки на кв.
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.moving_left = False

            if event.key == pygame.K_d:
                player.moving_right = False


    pygame.display.update()
        
        
#Вихід з програми
pygame.quit()