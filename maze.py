from abc import abstractmethod, ABC


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


class Wall():
    def __init__(self):
        self.north: int = 0
        self.east: int = 0
        self.south: int = 0
        self.west: int = 0


class Cell():
    def __init__(self):
        self.x: int = 0
        self.y: int = 0
        self.wall: Wall = Wall()


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


class Maze(ABC):
    def __init__(self):
        self.entry: Cell
        self.exit: Cell
        self.height: int
        self.width: int
    
    def config_maze(self, config_file: str):
        conf = ConfigTxt()
        conf.f_confing(config_file)
        self.entry = conf.entry
        self.exit = conf.exit
        self.height = conf.height
        self.width = conf.width

    def cell(self):
        cl: Cell = Cell()
        return cl

    def fill_maze(self) -> list[Cell]:
        maze: list[Cell] = []
        for i in range(0, self.width):
            for j in range(0, self.height):
                temp = self.cell()
                temp.x = i
                temp.y = j
                if j == 3:
                    temp.wall.north = 1
                    temp.wall.east = 1
                    temp.wall.south = 0
                elif j == 1:
                    temp.wall.north = 1
                    temp.wall.west = 0
                    temp.wall.south = 1
                else:
                    temp.wall.north = 0
                    temp.wall.west = 1
                    temp.wall.east = 1
                maze.append(temp)
        return maze
    
    def hexa_matrix(self, maze: list[Cell], file: str):
        hx = HexaMatrix()
        br_line = 0
        with open(file, "w") as fl:
            for cl in maze:
                fl.write(str(hx.binary_to_hexa(hx.string_wall(cl.wall))))
                if (br_line == (self.width - 1)):
                    fl.write("\n")
                    br_line = 0
                else:    
                    br_line += 1

    @abstractmethod
    def generate_maze(self):
        pass    


class ImperfectMaze(Maze):
    def generate_maze(self):
        pass


class PerfectMaze(Maze):
    def generate_maze(self):
        pass


mz = PerfectMaze()
"""mz.height = 4
mz.width = 37"""
mz.config_maze("config.txt")
maz = mz.fill_maze()
mz.hexa_matrix(maz, "ty.txt")