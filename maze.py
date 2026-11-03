from abc import abstractmethod, ABC


# Parede e uma fronte entre cellOne e cellTwo, podendo estar de pe ou nao
class Wall():
    def __init__(
            self,
            cellOne: tuple[int, int],
            cellTwo: tuple[int, int]
            ):
        self._cellOne: tuple[int, int] = cellOne
        self._cellTwo: tuple[int, int] = cellTwo
        self._up: bool = True

    def break_wall(self):
        self._up = False

    def regenerate(self):
        self._up = True


class Cell():
    def __init__(
            self, x: int, y: int
            ):
        self._visited: bool = False
        self._populed: bool = False
        self._cord: tuple[int, int] = (x, y)
        self._neighbors = {
            "Nort": (x, y - 1),
            "South": (x, y + 1),
            "East": (x + 1, y),
            "West": (x - 1, y)
        }
        self._wall: dict = {
            "Nort": True,
            "South": True,
            "East": True,
            "West": True
        }

    def break_wall(self, cordenate: str):
        self._wall[cordenate] = False

    def getting_in(self, cordenate: str):
        self._populed = True
        if self._wall[cordenate] == True:
            self.break_wall(cordenate)
        if self._visited == False:
            self._visited = True

    def getting_out(self, cordenate: str):
        self._populed = False
        if self._wall[cordenate] == True:
            self.break_wall(cordenate)


#        x=0     x=1     x=2     x=3
#     ┌───────┬───────┬───────┬───────┐
# y=0 │ (0,0) │ (1,0) │ (2,0) │ (3,0) │
#     ├───────┼───────┼───────┼───────┤
# y=1 │ (0,1) │ (1,1) │ (2,1) │ (3,1) │
#     ├───────┼───────┼───────┼───────┤
# y=2 │ (0,2) │ (1,2) │ (2,2) │ (3,2) │
#     ├───────┼───────┼───────┼───────┤
# y=3 │ (0,3) │ (1,3) │ (2,3) │ (3,3) │
#     └───────┴───────┴───────┴───────┘
class Matrix():
    def __init__(self,
                width: int, # x
                height: int # y
                ):
        self._width: int = width
        self._height: int = height
        self._cells: list[list[Cell]] = []
        self._walls: list[list[Wall]] = []

    def populate_cells(self):
        for y in range(self._height):
            row = []
            for x in range(self._width):
                row.append(Cell(x, y))
        self._cells.append(row)

    def frontier(self):
        #percorrer self._cells para calcular as paredess
        for y in range(self._height):
            row = []
            for x in range(self._width):
                # Criar Wall para East, se existir vizinho
                
                # Criar Wall para South, se existir vizinho

class ConfigTxt():
    def __init__(self):
        self.width: int = 0
        self.height: int = 0
        self.entry: tuple[int, int] = (0, 0)
        self.exit: tuple[int, int] = (0, 0)
        self.output_file: str = ""
        self.perfect = True

    def parser(self, file: str):
        return True

    def f_confing(self, file: str) -> None:
        content: list
        param: dict = {
            "WIDTH": self.width, "HEIGHT": self.height,
            "ENTRY": self.entry, "EXIT": self.exit,
            "OUTPUT_FILE": self.output_file, "PERFECT": self.perfect
            }
        if (self.parser(file)):
            try:
                with open(file, "r") as fl:

                    for line in fl:
                        content = line.strip().split("=")
                        if (content[0] in ["ENTRY", "EXIT"]):
                            temp: list = str(content[1]).split(",")
                            param[content[0]] = (int(temp[0]), int(temp[1]))
                        else:
                            param[content[0]] = content[1]

            except Exception:
                print("Invalid configuration file")

        else:
            print("Nothing happens")
   
        print(param)
        self.config_dinit(param)
    
    def config_dinit(self, param: dict):
        self.width = int(param["WIDTH"])
        self.height = int(param["HEIGHT"])
        self.entry = param["ENTRY"]
        self.exit = param["EXIT"]
        self.output_file = param["OUTPUT_FILE"]
        self.perfect = param["PERFECT"]        


class HexaMatrix():
    def string_wall(self, w: Wall) -> str:
        res: str = ""
        for i in [w.north, w.east, w.south, w.west]:
            res += str(i)
        return res

    def binary_to_hexa(self, binary: str) -> str | int:
        d_hexa = {
           "0000": 0, "0001": 1, "0010": 2, "0011": 3, "0100": 4,
           "0101": 5, "0110": 6, "0111": 7, "1000": 8, "1001": 9,
           "1010": "a", "1011": "b", "1100": "c", "1101": "d",
           "1110": "e", "1111": "f"
        }
        return d_hexa[binary]


# class Maze(ABC):
#     def __init__(self):
#         self.entry: Cell
#         self.exit: Cell
#         self.height: int
#         self.width: int
    
#     def config_maze(self, config_file: str):
#         conf = ConfigTxt()
#         conf.f_confing(config_file)
#         self.entry = conf.entry
#         self.exit = conf.exit
#         self.height = conf.height
#         self.width = conf.width

#     def cell(self):
#         cl: Cell = Cell()
#         return cl

#     def fill_maze(self) -> list[Cell]:
#         maze: list[Cell] = []
#         for i in range(0, self.width):
#             for j in range(0, self.height):
#                 temp = self.cell()
#                 temp.x = i
#                 temp.y = j
#                 if j == 3:
#                     temp.wall.north = 1
#                     temp.wall.east = 1
#                     temp.wall.south = 0
#                 elif j == 1:
#                     temp.wall.north = 1
#                     temp.wall.west = 0
#                     temp.wall.south = 1
#                 else:
#                     temp.wall.north = 0
#                     temp.wall.west = 1
#                     temp.wall.east = 1
#                 maze.append(temp)
#         return maze
    
    # def hexa_matrix(self, maze: list[Cell], file: str):
    #     hx = HexaMatrix()
    #     br_line = 0
    #     with open(file, "w") as fl:
    #         for cl in maze:
    #             fl.write(str(hx.binary_to_hexa(hx.string_wall(cl.wall))))
    #             if (br_line == (self.width - 1)):
    #                 fl.write("\n")
    #                 br_line = 0
    #             else:    
    #                 br_line += 1

    # @abstractmethod
    # def generate_maze(self):
    #     pass    


# mz = PerfectMaze()
# """mz.height = 4
# mz.width = 37"""
# mz.config_maze("config.txt")
# maz = mz.fill_maze()
# mz.hexa_matrix(maz, "ty.txt")