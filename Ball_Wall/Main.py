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
ignore = 0
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
    constant_pos = pygame.mouse.get_pos()
    (b,l) = constant_pos
    if b >= 950 or b <= 50 or l >= 950 or l <= 50:
        pass
    else:
        pos = True
    if line_draw is True:
        if pos == True:
            current_pos = pygame.mouse.get_pos()
            (b,l) = current_pos
            if b >= 950 or b <= 50 or l >= 950 or l <= 50:
                pos = False
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
                (z,r) = start
                if z >= 950 or z <= 50 or r >= 950 or r <= 50:
                    line_draw = False
                    STOP = True
                else:
                    line_draw = True
                    print("Start",start)    
         # Handle mouse button up (end drawing)
        if event.type == pygame.MOUSEBUTTONUP:
            if STOP == False:
                end = pygame.mouse.get_pos()
                line_draw = False
                print("End:", end)
                (x, y) = start
                direction = (end[0] - start[0], end[1] - start[1])
                magnitude = math.sqrt(direction[0] ** 2 + direction[1] ** 2)
                if magnitude != 0:
                    xvel = (direction[0] / magnitude) * speed
                    yvel = (direction[1] / magnitude) * speed

    #logic for bounce check
    if ignore>0:
         ignore = ignore-1
         print(ignore)
    else:
    #check if ball needs to bounce:
        if x >= 953-ballsize or x <= 47: #if ball is at left or right wall
                ignore= 3
                if xvel <=0.01:
                     xvel = -xvel
                else:
                    xvel = -xvel/slow_rate
        if y >= 953-ballsize or y <= 47:
                ignore = 3
                if yvel <=0.01:
                     yvel = -yvel
                else:
                    yvel = -yvel/slow_rate
    clock.tick(60)

    if line_draw == False:
        pygame.draw.ellipse(screen,WHITE,[x,y,ballsize,ballsize],0)
        x += xvel
        xvel = xvel/1.007
        y += yvel
        yvel= yvel/1.007

        pygame.display.update()
pygame.quit()
