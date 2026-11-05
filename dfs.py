#!python3
from maze import Matrix, Cell, Wall
import random


# Logica DFS:
#   Parametros = Celula inicial, Matrix montada
# 1. Escolha uma célula inicial e marque como visitada.
# 2. Observe os quatro vizinhos (Norte, Sul, Leste e Oeste).
# 3. Filtre os vizinhos que ainda não foram visitados.
# 4. Se houver vizinhos disponíveis:- Escolha um aleatoriamente.
#   - Quebre a parede entre a célula atual e a escolhida.
#   - Marque a nova célula como visitada.
#   - Avance para ela.
# 5. Se não houver vizinhos disponíveis:- Volte para a célula anterior.
#   - Continue procurando vizinhos não visitados.
# 6. Termine quando todas as células tiverem sido visitadas.

def is_border_land(cord: tuple[int, int], height: int, width: int) -> bool:
    x, y = cord
    if x < 0 or y < 0 or x > height or y > width:
        return True
    return False 

#Classe Jumper serve como representacao de alguem percorrendo as celulas
class Jumper():
    def __init__(self,
                first_cell: tuple[int, int]
                ):
        self._location: tuple[int, int] = first_cell
        self._trace: list[tuple[int, int]]
        self._compass: dict = {
            "Nort": (0, -1),
            "South": (0, 1),
            "East": (1, 0),
            "West": (-1, 0)
        }

    def move(self, direction: str):
        dx, dy = self._compass[direction]
        x, y = self._location
        self._location = (x + dx, y + dy)

def dfs(entry: tuple[int, int], exit: tuple[int, int], map: Matrix):
    x, y = entry
    compass: dict = {
        0: "Nort",
        1: "South",
        2: "East",
        3: "West"
    }

    if not (0 <= x < map._width and 0 <= y < map._height):
        raise ValueError("Invalid init cell")

    cell = map._cells[y][x]
    jumper = Jumper(cell._cord)

    while is_border_land(jumper._location, map._height, map._width):
        direction = random.randint(0, 3)
        jumper.move(compass[direction])
