import pygame
def draw_background(screen):
    global SCREEN_HEIGHT,SCREEN_WIDTH,GRID_WIDTH,BLACK
    rect_lines = [
        ((GRID_WIDTH, GRID_WIDTH), (GRID_WIDTH, SCREEN_HEIGHT - GRID_WIDTH)),
        ((GRID_WIDTH, GRID_WIDTH), (SCREEN_WIDTH - GRID_WIDTH, GRID_WIDTH)),
        ((GRID_WIDTH, SCREEN_HEIGHT - GRID_WIDTH),
         (SCREEN_WIDTH - GRID_WIDTH, SCREEN_HEIGHT - GRID_WIDTH)),
        ((SCREEN_WIDTH - GRID_WIDTH, GRID_WIDTH),
         (SCREEN_WIDTH - GRID_WIDTH, SCREEN_HEIGHT - GRID_WIDTH)),
    ]
    for line in rect_lines:
        pygame.draw.line(screen, (255,255,255), line[0], line[1], 2)
    for i in range(17):
        pygame.draw.line(screen, BLACK,
                         (GRID_WIDTH * (2 + i), GRID_WIDTH),
                         (GRID_WIDTH * (2 + i), SCREEN_HEIGHT - GRID_WIDTH))
        pygame.draw.line(screen, BLACK,
                         (GRID_WIDTH, GRID_WIDTH * (2 + i)),
                         (SCREEN_HEIGHT - GRID_WIDTH, GRID_WIDTH * (2 + i)))
    circle_center = [
        (GRID_WIDTH * 4, GRID_WIDTH * 4),
        (SCREEN_WIDTH - GRID_WIDTH * 4, GRID_WIDTH * 4),
        (SCREEN_WIDTH - GRID_WIDTH * 4, SCREEN_HEIGHT - GRID_WIDTH * 4),
        (GRID_WIDTH * 4, SCREEN_HEIGHT - GRID_WIDTH * 4),
        (GRID_WIDTH * 10, GRID_WIDTH * 10)
    ]
    for cc in circle_center:
        pygame.draw.circle(screen, BLACK, cc, 5)
SCREEN_WIDTH,SCREEN_HEIGHT = 720,720
GRID_WIDTH = SCREEN_WIDTH//20
FPS = 30
BLACK = (255,255,255)
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("五子棋")
screen.fill((249,204,226))
clock = pygame.time.Clock()
movements = []
chessman = [[None] * 20 for i in range(20)]
def add_coin(grid,color,user):
    movements.append(((grid[0] * GRID_WIDTH,grid[1] * GRID_WIDTH),color))
    chessman[grid[1]][grid[0]] = user
def draw_movements(screen):
    for m in movements:
        pygame.draw.circle(screen,m[1],m[0],12)
def judgement(x,y,color):
    global chessman
    horizon = 1
    vertical = 1
    slash = 1
    backslash = 1
    left = y - 1
    while left > 0 and chessman[x][left] == color:
        horizon += 1
        left -= 1
    right = y + 1
    while right < 20 and chessman[x][right] == color:
        horizon += 1
        right += 1
    up = x - 1
    while up > 0 and chessman[up][y] == color:
        vertical += 1
        up -= 1
    down = x + 1
    while down < 20 and chessman[down][y] == color:
        vertical += 1
        down += 1
    left = y - 1
    up = x - 1
    while left > 0 and up > 0 and chessman[up][left] == color:
        backslash += 1
        left -= 1
        up -= 1
    right = y + 1
    down = x + 1
    while right < 20 and down < 20 and chessman[down][right] == color:
        backslash += 1
        right += 1
        down += 1
    left = y - 1
    down = x + 1
    while left > 0 and down < 20 and chessman[down][left] == color:
        slash += 1
        left -= 1
        down += 1
    right = y + 1
    up = x - 1
    while right < 20 and up > 0 and chessman[up][right] == color:
        slash += 1
        right += 1
        up -= 1
    if max([horizon,vertical,slash,backslash]) >= 5:
        return True
running = True
turn = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if turn == True:
                pos = event.pos
                grid = (int(round(event.pos[0] / (GRID_WIDTH + .0))),int(round(event.pos[1] / GRID_WIDTH + .0)))
                add_coin(grid,(0,0,0),"black")
                if judgement(grid[1],grid[0],"black"):
                    running = False
            if turn == False:
                pos = event.pos
                grid = (int(round(event.pos[0] / (GRID_WIDTH + .0))), int(round(event.pos[1] / GRID_WIDTH + .0)))
                add_coin(grid, (255, 255, 255),"white")
                if judgement(grid[1], grid[0], "white"):
                    running = False
        draw_background(screen)
        draw_movements(screen)
        pygame.display.flip()
