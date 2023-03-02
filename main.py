import pygame

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
screenColor = (255, 255, 255)
rectColor = (0, 0, 0)
rectSize = rectWidth, rectHeight = 10, 100
rectPos = rectX, rectY = 5, 200
rectPos2 = rectX2, rectY2 = 485, 200
rectSpeed = 2
gameRect = pygame.Rect(rectX, rectY, rectWidth, rectHeight)
gameRect2 = pygame.Rect(rectX2, rectY2, rectWidth, rectHeight)
ballColor = (0, 0, 0)
ballSize = ballWidth, ballHeight = 10,10
ballPos = ballX, ballY = 250, 250
ballSpeed = 1
x_speed = -2
y_speed = 1
playerA_score = 0
playerB_score = 0
keyPress = False
#mytuple = playerA_score, playerB_score
ball = pygame.Rect(ballX, ballY, ballWidth, ballHeight)
clock = pygame.time.Clock()
textScore = str(playerA_score) + " Score " + str(playerB_score)
#ballSize =
#'%d Score %d' %mytuple
pygame.init()
pygame.display.set_caption("Pong Game")
surface = pygame.display.set_mode(SCREEN_SIZE)
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render(textScore, True, rectColor)
text_Rect = text.get_rect()
text_Rect.center = (500//2, 50)

def move_rect(gameRect):
    if keys[pygame.K_UP]:
        gameRect2.move_ip(0, -rectSpeed)
    elif keys[pygame.K_DOWN]:
        gameRect2.move_ip(0, rectSpeed)

def move_rect2(gameRect2):
    if keys[pygame.K_w]:
        gameRect.move_ip(0, -rectSpeed)
    elif keys[pygame.K_s]:
        gameRect.move_ip(0, rectSpeed)

def game_reset():
    ball.update(ballX, ballY, ballWidth, ballHeight)
    gameRect.update(rectX, rectY, rectWidth, rectHeight)
    gameRect2.update(rectX2, rectY2, rectWidth, rectHeight)
    keyPress = 0
    # x_speed = 0
    # y_speed = 0


#Game Loop
while True:
    for event in pygame.event.get():  #Listening for Events (key press, times, etc)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(screenColor)
    surface.blit(text, text_Rect)
    keys = pygame.key.get_pressed()
    move_rect(gameRect)
    move_rect2(gameRect2)
    gameRect.clamp_ip(surface.get_rect())
    gameRect2.clamp_ip(surface.get_rect())
    ball.clamp_ip(surface.get_rect())
    pygame.draw.rect(surface, rectColor, gameRect)
    pygame.draw.rect(surface, rectColor, gameRect2)
    pygame.draw.rect(surface, ballColor, ball)
    #flag for keypress

    if keyPress == False:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball.move_ip(x_speed, y_speed)
                keyPress = True
            elif event.key == pygame.K_DOWN:
                ball.move_ip(x_speed, y_speed)
                keyPress = True
            elif event.key == pygame.K_w:
                ball.move_ip(x_speed, y_speed)
                keyPress = True
            elif event.key == pygame.K_s:
                ball.move_ip(x_speed, y_speed)
                keyPress = True
    else:
        ball.move_ip(x_speed, y_speed)


    if ball.right >= SCREEN_WIDTH:
        #y = list(mytuple)
        #y[1] = playerA_score + 1
        #mytuple = tuple(y)
        playerA_score += 1
        textScore = str(playerA_score) + " Score " + str(playerB_score)
        game_reset()
    if ball.left <= 0:
        playerB_score += 1
        textScore = str(playerA_score) + " Score " + str(playerB_score)
        #y = list(mytuple)
        #y[1] = playerB_score + 1
        #mytuple = tuple(y)
        game_reset()
    if ball.bottom >= SCREEN_HEIGHT or ball.top <= 0:
        y_speed *= -1
    if ball.colliderect(gameRect) or ball.colliderect(gameRect2):
        x_speed *= -1
    #text = font.render('%d Score %d' %mytuple , True, rectColor)
    surface.blit(text, text_Rect)
    text = font.render(textScore, True, rectColor)

    pygame.display.update()
