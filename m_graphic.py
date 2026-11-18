import pygame


class maze_graphics():
    def __init__(self, params: dict):
        pygame.init()
        self.param = params
        self.screen = pygame.display.set_mode(
            (self.param["width"]*self.param["cell_w"],
                self.param["height"]*self.param["cell_h"]))
        self.clock = pygame.time.Clock()
        self.border_thickness = self.param["border"]
        self.rect_h = self.param["cell_h"]
        self.rect_w = self.param["cell_w"]

    def color(self, clr: str):
        GREEN = (0, 255, 0)
        PURPLE = (90, 76, 170)
        RED = (255, 0, 0)
        BLUE = (0, 0, 255)
        colors = {
            "green": GREEN,
            "red": RED,
            "blue": BLUE,
            "purple": PURPLE
        }
        return colors[clr]
         
    def get_maze(self, maze: str) -> str:
        res: str
        with open(maze, "r") as file:
            res = file.read()
        return res.replace("\n", "").replace(" ", "")

    def hexa_decoder(self, hexa: str) -> str:
        h_values = {
           "0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100",
           "5": "0101", "6": "0110", "7": "0111", "8": "1000", "9": "1001",
           "a": "1010", "b": "1011", "c": "1100", "d": "1101", "e": "1110",
           "f": "1111"
        }
        return h_values[hexa]

    def draw_retangles(self, color: str) -> None:
        for i in range(self.param["height"]):
            for j in range(self.param["width"]):
                pygame.draw.rect(self.screen, self.color(color),
                                 (j * self.rect_w, i * self.rect_h,
                                  self.rect_w, self.rect_h))

    def draw_maze(self, maze: str, color: str) -> None:
        width = self.param["width"]
        count = 0
        x = 0
        y = 0
        cl = self.color(color)
        self.draw_retangles("green")
        for i in range(self.param["height"]):
            for j in range(width):
                count = i * width + j
                if count >= len(maze):
                    return
                x = j * self.rect_w
                y = i * self.rect_h
                temp: str = self.hexa_decoder(maze[count])
                if (temp[0] == "1"):
                    pygame.draw.line(self.screen, cl, (x + self.rect_w, y),
                                     (x + self.rect_w, y + self.rect_h),
                                     self.border_thickness)
                if (temp[1] == "1"):
                    pygame.draw.line(self.screen, cl, (x, y + self.rect_h),
                                     (x + self.rect_w, y + self.rect_h),
                                     self.border_thickness)
                if (temp[2] == "1"): 
                    pygame.draw.line(self.screen, cl, (x, y),
                                     (x, y + self.rect_h),
                                     self.border_thickness)
                if (temp[3] == "1"):
                    pygame.draw.line(self.screen, cl, (x, y),
                                     ((x + self.rect_w, y)),
                                     self.border_thickness)
                    
    def display_maze(self, f_name: str):
        pygame.display.set_caption("A-MAZING")
        running = True
        maze = self.get_maze(f_name)
        while running:  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill("white")
            self.draw_maze(maze, "blue")    
            self.clock.tick(60)
            pygame.display.flip()
        pygame.quit()


param = {
     "height": 20,
     "width": 25,
     "cell_w": 34,
     "cell_h": 34,
     "border": 4
     }

mz = maze_graphics(param)
mz.display_maze("ny.txt")
