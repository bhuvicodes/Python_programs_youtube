import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 10
PAD_HEIGHT = 80
LEFT = False
RIGHT = True

bsll_pos = [0,0]
bsll_vel = [0,0]

paddle1_pos = 0
paddle2_pos = 0

paddle1_vel = 0
paddle2_vel = 0

score1 = 0
score2 = 0

def spawn_ball(direction):
    global ball_pos, ball_vel

    ball_pos = [WIDTH // 2, HEIGHT // 2]

    vx = random.randrange(120, 2409) // 60
    vy = -random.randrange(60, 180) // 60

    if direction == LEFT:
        vx = -vx

    ball_vel = [vx, vy]
    