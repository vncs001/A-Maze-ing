import pygame


class maze_graphics():
    """To be implemented """


pygame.init()
#O tamanho da janela vai depender do cell size
screen = pygame.display.set_mode((1001, 800))
clock = pygame.time.Clock()
pygame.display.set_caption("A-MAZING")
GREEN = (0, 255, 0)
RED = (90, 76, 170)
BLUE = (0, 0, 255)
border_thickness = 4
rect_h = 40
rect_w = 40


def get_maze(maze: str) -> str:
    res: str
    with open(maze, "r") as file:
        res = file.read()
    return res.replace("\n", "").replace(" ", "")


def hexa_decoder(hexa: str) -> str:
    h_values = {
        "0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100",
        "5": "0101", "6": "0110", "7": "0111", "8": "1000", "9": "1001",
        "a": "1010", "b": "1011", "c": "1100", "d": "1101", "e": "1110",
        "f": "1111"
    }
    return h_values[hexa]


def draw_retangles(width: int, height: int) -> None:
    for i in range(height):
        for j in range(width):
            pygame.draw.rect(screen, RED,
                             (j * rect_w, i * rect_h, rect_w, rect_h))


def draw_maze(maze: str) -> None:
    width = 25
    height = 20
    count = 0
    x = 0
    y = 0
    draw_retangles(width, height)
    for i in range(height):
        for j in range(width):
            count = i * width + j
            if count >= len(maze):
                return
            x = j * rect_w
            y = i * rect_h
            temp: str = hexa_decoder(maze[count])
            if (temp[0] == "1"):
                pygame.draw.line(screen, GREEN, (x, y),
                                 ((x + rect_w, y)), border_thickness)
            if (temp[1] == "1"):
                pygame.draw.line(screen, GREEN, (x + rect_w, y),
                                 (x + rect_w,
                                 y + rect_h), border_thickness)
            if (temp[2] == "1"): 
                pygame.draw.line(screen, GREEN, (x, y + rect_h),
                                 (x + rect_w,
                                 y + rect_h), border_thickness)
            if (temp[3] == "1"):
                pygame.draw.line(screen, GREEN, (x, y),
                                 (x, y + rect_h), border_thickness)


running = True
maze = get_maze("ny.txt")
while running:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    draw_maze(maze)    
    clock.tick(60)
    pygame.display.flip()
pygame.quit()
