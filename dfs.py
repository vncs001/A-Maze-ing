#!python3
from maze import Matrix, Cell, Wall
import random
from explorer import Explorer

# ALGORITMOS PARA PROCURAR
# 1. BFS Procurar
# 2. Hunting and kill
# 3. Prims

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


def valid_directions(
        cord: tuple[int, int],
        map: Matrix
    ) -> list[str]:

    x, y = cord
    height = map._height
    width = map._width
    neighbors = {
        "North": (x, y - 1),
        "South": (x, y + 1),
        "East": (x + 1, y),
        "West": (x - 1, y)
    }

    compass = {}

    for direction, (nx, ny) in neighbors.items():
        if 0 <= nx < width and 0 <= ny < height:
            compass[direction] = not map._cells[ny][nx].visited
        else:
            compass[direction] = False

    available = [
        direction
        for direction, is_valid in compass.items()
            if is_valid
    ]
    return available


def dfs(entry: tuple[int, int], exit: tuple[int, int], map: Matrix):
    x, y = entry

    if not (0 <= x < map._width and 0 <= y < map._height):
        raise ValueError("Invalid init cell")

    cell = map._cells[y][x]
    cell.visit()
    stack = [cell]

    while stack:
        cell = stack[-1]
        available = valid_directions(cell._cord, map)

        if available:

            direction = random.choice(available)

            # Aqui você precisará obter a célula vizinha.
            x, y = cell._neighbors[direction] 
            nextCell = map._cells[y][x]
            # Depois quebrar a parede entre as células.
            map.carve_path(cell, direction)
            cell._wall[direction] = False
            
            # Marcar vizinha como visitada.
            nextCell.visit()
            # Adicionar vizinha na pilha.
            stack.append(nextCell)
            pass

        else:
            stack.pop()

    map.print_matrix()
    map.write_hxmatrix("result.txt")
    # explorer = Explorer(cell._cord)
    # compass = valid_directions(cell._cord, map)
    # available = [
    #     direction
    #     for direction, is_valid in compass.items()
    #         if is_valid
    # ]
    # direction = random.choice(available)

    # print(compass)
#-----------------
    # while not is_border_land(explorer._location, map._height, map._width):
    #     explorer.move(compass[direction])
    #     # querbra parede
    #     x, y = explorer._location 
    #     nextCell = map._cells[y][x]
    #     map.carve_path(cell, direction)
    #     if not cell._visited:
    #         cell.visit()
    #     cell = nextCell
    #     map.print_matrix()

