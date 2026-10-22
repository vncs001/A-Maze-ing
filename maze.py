from abc import abstractmethod, ABC


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


class Maze(ABC):
    def __init__(self):
        self.entry: Cell
        self.exit: Cell
        self.height: int
        self.width: int

    @abstractmethod
    def config_file(self):
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


h = HexaMatrix()
w = Wall()
w.north = 1
w.south = 1
print(h.string_wall(w))
print(h.binary_to_hexa(h.string_wall(w)))
