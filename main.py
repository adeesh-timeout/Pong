import pygame#
import random
import os

# Change Directory # Random Error 01
os.chdir(os.path.dirname(os.path.abspath(__file__)))

run = True

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
ICON = pygame.image.load('pong_icon.png')
LINE_HEIGHT = 50
LINE_GAP = 20

WIDTH = 15
HEIGHT = 100

VELOCITY = 5

ball_x_vel = random.choice([-1,1]) * 5
ball_y_vel = random.choice([-1,1]) * 5

player1_score = player2_score = 0

player1_x = 10
player1_y = (SCREEN_HEIGHT//2)-50

player2_x = SCREEN_WIDTH-WIDTH-player1_x
player2_y = (SCREEN_HEIGHT//2)-50

ball_x = 400
ball_y = 300 
RADIUS = 10

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_icon(ICON)
pygame.display.set_caption("Pong")

def draw_objects():
    pygame.draw.circle(screen, (255,255,255), (ball_x,ball_y), RADIUS)
    pygame.draw.rect(screen, (255,255,255), (player1_x,player1_y, WIDTH,HEIGHT))
    pygame.draw.rect(screen, (255,255,255), (player2_x,player2_y, WIDTH,HEIGHT))

def check_ball_collision():
    global ball_x, ball_y, ball_x_vel, ball_y_vel, player2_score, player1_score

    # Paddle
    if ball_x-RADIUS < player1_x+WIDTH and player1_y < ball_y and player1_y + HEIGHT > ball_y:
        ball_x_vel = -ball_x_vel

    elif ball_x+RADIUS > player2_x and player2_y < ball_y and player2_y + HEIGHT > ball_y:
        ball_x_vel = -ball_x_vel

    if ball_y - RADIUS <= 0:
        ball_y_vel = -ball_y_vel 

    # Bottom wall
    elif ball_y + RADIUS >= SCREEN_HEIGHT:
        ball_y_vel = -ball_y_vel

    if ball_x - RADIUS <= 0:
        ball_x_vel = -ball_x_vel
        player2_score += 1

    # Right wall
    elif ball_x + RADIUS >= SCREEN_WIDTH:
        ball_x_vel = -ball_x_vel
        player1_score += 1

    ball_x += ball_x_vel
    ball_y += ball_y_vel

    text = font_1.render(str(player1_score), 1, 'white')
    screen.blit(text, (200,50))

    text = font_1.render(str(player2_score), 1, 'white')
    screen.blit(text, (600,50))

font_1 = pygame.font.SysFont('Lucida console', 60)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    screen.fill((0,0,0))

    if keys[pygame.K_w] and player1_y-VELOCITY > 0:
        player1_y -= VELOCITY
    
    elif keys[pygame.K_s] and player1_y+VELOCITY+HEIGHT < SCREEN_HEIGHT:
        player1_y += VELOCITY
    
    if keys[pygame.K_UP] and player2_y-VELOCITY > 0:
        player2_y -= VELOCITY
    
    elif keys[pygame.K_DOWN] and player2_y+VELOCITY+HEIGHT < SCREEN_HEIGHT:
        player2_y += VELOCITY

    # Draws Line
    for i in range(0, 9):
        pygame.draw.line(screen, (255,255,255), (SCREEN_WIDTH//2, LINE_GAP*i+LINE_HEIGHT*i), (400,50*(i+1)+LINE_GAP*i), 3)    

    draw_objects()
    check_ball_collision()
    
    pygame.display.update()
    clock.tick(FPS)