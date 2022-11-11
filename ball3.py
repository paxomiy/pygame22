import pygame
from pygame.draw import *
from random import randint
pygame.init()

maxnumber=10 #максимальное количество шаров
smile_speed_y=13#скорость смайла
smile_speed_x=10#скорость смайла
smile_x = randint(0,400)#начальная координата х смайла
smile_y = randint(0,400) #начальная координата по у смайла
smile_speed = 15 # скорость смайла
FPS = 30 #FPS
screen = pygame.display.set_mode((800, 600))#рахмер экрана
scores = 0 #очки
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN] #возможные цвета
speed_x=[]#скорости шаров
speed_y=[]#скорости шаров
balls=[]
r=[]
smile=pygame.image.load('smile.png').convert()#
smile_box=smile.get_rect()
def new_balls():    #создание шаров
    global x, y, r, speed_x, speed_y, balls,number
    number = randint(1, maxnumber)
    for i in range(number):
        x = randint(100, 700)
        y = randint(100, 500)
        r.append(randint(30, 50))
        balls.append([x, y])
        color = COLORS[randint(0, 5)]
        circle(screen, COLORS[i%6], (balls[i]), r[i])
def update_position(): #перемещение шаров с отскоками
    global x, y, r, speed_x, speed_y, balls
    for i in range(number):
        speed_x.append(randint(20, 30))
        speed_y.append(randint(20, 30))

        circle(screen, COLORS[i%6], (balls[i]), r[i])
        balls[i][1] += speed_y[i]
        balls[i][0] += speed_x[i]
        if balls[i][0] + r[i] >= 800:
            speed_x[i] = speed_x[i] * (-1)
        if balls[i][0] - r[i] <= 0:
            speed_x[i] = speed_x[i] * (-1)
        if balls[i][1] - r[i] <= 0:
            speed_y[i] = speed_y[i] * (-1)
        if balls[i][1] + r[i] >= 600:
            speed_y[i] = speed_y[i] * (-1)
def Smile():#смайл
    global smile,smile_x,smile_y,smile_speed,smile_speed_x,smile_speed_y
    screen.blit(smile, (smile_x, smile_y))
    smile_y += smile_speed_y * 3 / 5
    smile_x += smile_speed_x
    if smile_x + 190 >= 800:
        smile_speed_x = smile_speed_x * (-1)
        smile_speed_y = smile_speed_y + randint(0,15)*randint(-1,1)
    if smile_x <= 0:
        smile_speed_x = smile_speed_x * (-1)
        smile_speed_y = smile_speed_y + randint(0,15)*randint(-1,1)
    if smile_y + 190 >= 600:
        smile_speed_y = smile_speed_y * (-1)
        smile_speed_x = smile_speed_y + randint(0,15)*randint(-1,1)
    if smile_y <= 0:
        smile_speed_y = smile_speed_y * (-1)
        smile_speed_x = smile_speed_y + randint(0,15)*randint(-1,1)
def SmileClick(event):#попадание по смайлу
    global scores
    if (abs(event.pos[0]-smile_x)<=smile_box[2]) and (abs(event.pos[1]-smile_y)<=smile_box[3]):
        scores+=2
        print("попал")
        return scores

def click(event): #счетчик очков
    global scores,f1,text1
    for i in range(number):
        if((balls[i][0]-event.pos[0])**2+(balls[i][1]-event.pos[1])**2)<=r[i]**2:
            scores += 1

            return scores
def click2(event): # условие попадания по шару
    for i in range(number):
        if((balls[i][0]-event.pos[0])**2+(balls[i][1]-event.pos[1])**2)<=r[i]**2:

            return True

pygame.display.update()
clock = pygame.time.Clock()#часы

finished = False
new_balls()#начальный выброс шаров
while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
            print('Click!', 'scores=', scores)
            click(event)    #очки по кликам
            SmileClick(event)       # очки по смайлу
            if click2(event)==True:
                balls=[]
                new_balls()

                print("попал")



    screen.fill(BLACK)
    f1 = pygame.font.Font(None, 50)
    text1 = f1.render('scores'+str(scores), True, (255, 255, 255))
    screen.blit(text1, (20, 30))
    pygame.display.update()
    update_position()
    Smile()
    pygame.display.update()




pygame.quit()