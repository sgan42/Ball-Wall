import pygame
import math
z=0
r=0
b=0
l=0
STOP = False
pos = False
clock = pygame.time.Clock()
stack = []
WHITE = (255,255,255)
BLACK = (0,0,0)
x = 500
y = 500
xvel = 4
yvel = 6
ballsize = 60
start = (50,50)
current_pos = (50,50)
end = 2
line_draw = False
speed = 35
slow_rate =1.7
#game display
pygame.init()
screen = pygame.display.set_mode((1000,1000))
screen.fill(BLACK)
pygame.display.set_caption('The Bouncing Ball')

#walls
def draw_walls():
    floor = pygame.draw.line(screen, WHITE, (950,950), (50,950),8)
    ceiling = pygame.draw.line(screen, WHITE, (50, 50), (950,50),8)
    wall_left = pygame.draw.line(screen, WHITE, (50, 50), (50, 950),8)
    wall_right = pygame.draw.line(screen, WHITE, (950,950), (950,50),8)

#game run
rungame = True
while rungame:
    screen.fill(BLACK)
    draw_walls()
    if line_draw is True:
        current_pos = pygame.mouse.get_pos()
        pygame.draw.line(screen,WHITE, start, current_pos,6)  # Draw the line dynamically
        pygame.display.update()
        print("Current position:", current_pos)  # Print the current mouse position
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rungame = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                start = pygame.mouse.get_pos()
                STOP = False
                pos = True
                (x,y) = start
                if x >= 950 or x <= 50 or y >= 950 or y <= 50:
                    line_draw = False
                    STOP = True
                else:
                    line_draw = True
                    print("Start",start)    
         # Handle mouse button up (end drawing)
        if event.type == pygame.MOUSEBUTTONUP:
            if STOP == False:
                # (b,l) = current_pos
                # if b > 950:
                #     end = (950,l)
                # if l > 950:
                #     end = (b,950)
                end = pygame.mouse.get_pos()
                line_draw = False
                print("End:", end)
                (x, y) = start
                direction = (end[0] - start[0], end[1] - start[1])
                magnitude = math.sqrt(direction[0] ** 2 + direction[1] ** 2)
                if magnitude != 0:
                    xvel = (direction[0] / magnitude) * speed
                    yvel = (direction[1] / magnitude) * speed

    # Bounce logic:
    if x + ballsize > 950:
        x = 950 - ballsize
        xvel = -xvel / slow_rate
    elif x < 50:
        x = 50 
        xvel = -xvel / slow_rate

    if y + ballsize > 950:
        y = 950 - ballsize
        yvel = -yvel / slow_rate
    elif y < 50:
        y = 50
        yvel = -yvel / slow_rate
    clock.tick(60)

    if line_draw == False:
        pygame.draw.ellipse(screen,WHITE,[x,y,ballsize,ballsize],0)
        x += xvel
        y += yvel

        xvel = xvel/1.007
        yvel= yvel/1.007

        pygame.display.update()
pygame.quit()
