from abc import abstractmethod, ABC


class ConfigTxt():
    """
    WIDTH=20
    HEIGHT=15
    ENTRY=0,0
    EXIT=19,14
    OUTPUT_FILE=maze.txt
    PERFECT=True
    """

    def __init__(self):
        self.width: int
        self.height: int
        self.entry: tuple[int, int]
        self.exit: tuple[int, int]
        self.output_file: str
        self.perfect = True

    def parser(self):
        pass
    
    def f_confing(self, file: str):
        content: list
        param: dict = {
            "WIDTH": self.width, "HEIGHT": self.height,
            "ENTRY": self.entry, "EXIT": self.exit,
            "OUTPUT_FILE": self.output_file, "PERFECT": self.perfect
            }
        print(param)
        if (self.parser(file)):
            try:
                with open(file, "r") as fl:
                    content = fl.readline().split("=")
                    if (content[0] == "ENTRY" or content[0] == "EXIT"):
                        temp: list = str(content[1]).split(",")
                        param[content[0]] = (temp[0], temp[1])
                    else:
                        param[content[0]] = content[1]
            except Exception:
                print("Invalid configuration file")


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
        self.wall: Wall


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
    
    def cell(self):
        cl: Cell = Cell()
        return cl

    def init_maze(self):
        config = ConfigTxt()
        maze: list = []
        print(config)
        for i in range(0, self.width):
            for j in range(0, self.height):
                temp = self.cell()
                temp.x = i
                temp.y = j
                maze.append(temp)
        return maze
    
    def hexa_matrix(maze: list, file: str):
        hx = HexaMatrix()
        with open(file, "w") as fl:
            for cl in maze:
                fl.write(hx.binary_to_hexa(hx.string_wall(cl.w)))
        pass

    @abstractmethod
    def generate_maze(self):
        pass    


class ImperfectMaze(Maze):
    def generate_maze(self):
        pass


class PerfectMaze(Maze):
    def generate_maze(self):
        pass


h = HexaMatrix()
w = Wall()
w.north = 1
w.south = 1
print(h.string_wall(w))
print(h.binary_to_hexa(h.string_wall(w)))

print("Reading the file .......")
ct = ConfigTxt()
ct.config_file("config.txt")