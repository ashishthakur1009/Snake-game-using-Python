#pip install pygame
import pygame, random
pygame.init()

width = 600
height = 300
screen = pygame.display.set_mode((width, height))
frog = pygame.image.load("frog.png")
sound = pygame.mixer.Sound('ahem_x.wav')

#rgb - red, green, blue
#0-255, 0-255, 0-255
RED = 255,0,0
BLUE = 0,0,255
YELLOW = 255,255,0
BLACK = 0,0,0
WHITE = 255,255,255
x = 0
y = 0
x2 = random.randint(0,width - 50)
y2 = random.randint(0,height - 50)
moveX = 1
moveY = 0
counter = 0
snakeWidth = 50
snakeBody = []
requiredLength = 1

def displayScore():
    msg = "Score : {}".format(counter)
    font = pygame.font.SysFont(None, 25, True, True)
    #msg, antialias (smoothening of characters), text color, bgcolor 
    score = font.render(msg, True, RED, None)
    screen.blit(score, (0,0))

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                moveY = 1
                moveX = 0
            elif event.key == pygame.K_UP:
                moveY = -1
                moveX = 0
            elif event.key == pygame.K_LEFT:
                moveX = -1
                moveY = 0
            elif event.key == pygame.K_RIGHT:
                moveX = 1
                moveY = 0

    screen.fill( WHITE )
    #surface, color, (x,y,width,height)
    rect1 = pygame.draw.rect(screen, RED, (x,y,snakeWidth,50))
    screen.blit(frog, (x2,y2))
    # rect2 = pygame.draw.rect(screen, BLACK, (x2,y2,50,50))
    # pygame.draw.rect(screen, BLUE, (x2 - 50,y2 - 50,100,100))
    rect2 = pygame.Rect(x2, y2 , 50, 50)
    # pygame.draw.circle(screen, BLACK, (x2,y2), 50)

    snakeHead = x,y
    (5,3)

    snakeBody.append(snakeHead)

    if len(snakeBody) > requiredLength:  
        del snakeBody[0]
    print(snakeBody)

    for bodyPart in snakeBody:
        pygame.draw.rect(screen, RED, (bodyPart[0],bodyPart[1],snakeWidth,50))
    
    displayScore()

    if rect1.colliderect(rect2):
        x2 = random.randint(0,width - 50)
        y2 = random.randint(0,height - 50)  
        sound.play()
        counter += 1
        # snakeWidth += 25
        requiredLength += 100

    #surface, color, (x,y), radius
    # pygame.draw.circle(screen, RED, (x,y), 50)
    x += moveX
    y += moveY

    if x < -50:
        x = width
    elif y < -50:
        y = height
    elif x > width:
        x = -50
    elif y > height:
        y = -50

    # if y > height - 50:
    #     moveY = -1
    # elif y < 0:
    #     moveY = 1
    # elif x > width - 50:
    #     moveX = -1
    # elif x < 0:
    #     moveX = 1

    pygame.display.update()
