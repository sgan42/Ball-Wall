import pygame

clock = pygame.time.Clock()
WHITE = (255,255,255)
BLACK = (0,0,0)
x = 500
y = 500
xvel = 2
yvel = 3
ballsize = 10
start = 1
end = 1
line_draw = False
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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rungame = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                start = pygame.mouse.get_pos()
                line_draw = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if pygame.mouse.get_pressed()[0]:
                end = pygame.mouse.get_pos()
                line_draw = False
        
    #check if ball needs to bounce:
    if x >= 950-ballsize or x <= 50: #if ball is at left or right wall
        xvel = -xvel        #change direction
    if y >= 950-ballsize or y <= 50: #if ball is at top or bottom:
        yvel = -yvel        #change direction
    clock.tick(60)
    


            #pygame.draw.line(screen, WHITE, (start), (end),8)
    print(start)
    print(end)
    screen.fill(BLACK)
    draw_walls()
    pygame.draw.ellipse(screen,WHITE,[x,y,ballsize,ballsize],0)
    x += xvel #make x go up by xvel
    y += yvel #make y go up by yvel
    pygame.display.update()
pygame.quit()
