#Classe explorer serve como representacao de alguem percorrendo as celulas
class Explorer():
    def __init__(self,
                first_cell: tuple[int, int]
                ):
        self._location: tuple[int, int] = first_cell
        self._trace: list[tuple[int, int]]
        self._compass: dict = {
            "North": (0, -1),
            "South": (0, 1),
            "East": (1, 0),
            "West": (-1, 0)
        }

    def move(self, direction: str):
        dx, dy = self._compass[direction]
        x, y = self._location
        self._location = (x + dx, y + dy)
