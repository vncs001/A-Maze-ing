from maze import Matrix, Cell
from collections import deque
import explorer
import random

# LOGICA BFS:
#   - Percorre todos os caminhos em paralelo e salva a rota percorrida
#   - Compara qual caminho de A ate Z e o menor
# PASSOS BFS:
#    1. Inicialização   
#       [x] Identificar Entry e Exit (coordenadas (x, y)).
#       [x] Criar a fila (deque) contendo só a Entry.
#       [x] Criar visited (set) contendo só a Entry.
#       [x] Criar came_from vazio (dict: célula -> (célula_anterior, direção)).
#    2. Exploração
#    Enquanto a fila não estiver vazia:
#       [x] Tirar a célula da FRENTE da fila (popleft).
#       [x] Se ela for a Exit, parar o laço.
#       [ ] Para cada direção (North, East, South, West):
#           [x] Calcular o vizinho (nx, ny).
#           [x] Pular se estiver fora do grid.
#           [ ] Pular se houver parede nessa direção.
#           [ ] Pular se o vizinho já estiver em visited.
#           [ ] Marcar o vizinho em visited.
#           [ ] Guardar came_from[vizinho] = (atual, direção).
#           [ ] Colocar o vizinho no FIM da fila (append).
#    3. Reconstrução do caminho
#       [ ] Se a Exit não está em came_from, não existe caminho (tratar).
#       [ ] Começar na Exit e seguir came_from até chegar na Entry,
#           guardando a letra de cada direção (N, E, S, W).
#       [ ] Inverter a lista (você montou de trás pra frente).
#       [ ] Juntar numa string, ex.: "EESSWN".
#    4. Validação
#       [ ] Testar num 3x3 à mão: o caminho tem o tamanho esperado?
#       [ ] Andar o caminho a partir da Entry e conferir que nenhum passo
#           atravessa parede e que termina na Exit.


def valid_directions(
        cord: tuple[int, int],
        map: Matrix
    ) -> list[str]:

    x, y = cord
    height = map._height
    width = map._width
    neighbors = {
        "North": (x, y - 1),
        "East": (x + 1, y),
        "South": (x, y + 1),
        "West": (x - 1, y), 
    }

    compass = {}

    for direction, (nx, ny) in neighbors.items():
        if (0 <= nx < height and 0 <= ny < width) and (not map._cells[ny][nx].valid):
            compass[direction] = map._cells[ny][nx].has_wall(direction) #verifica se existe passagem pela direcao
        else:
            compass[direction] = False

    available = [
        direction
        for direction, is_valid in compass.items()
            if is_valid
    ]
    return available


def oposite_wall(direction: str):
    oposite = {
        "North": "South",
        "East": "West",
        "South": "North",
        "West": "East",
    }
    return oposite[direction]


def take_neighbor(cell: Cell, direction: str, map: Matrix):
    directions = valid_directions(cell._cord, map)
    for dir in directions:
        if dir == direction:
            return cell._neighbors[direction]


def bfs(entry: tuple[int, int], exit: tuple[int, int], map: Matrix):
    x, y = entry

    if not (0 <= x < map._width and 0 <= y < map._height):
        raise ValueError("Invalid init cell")

    cell = map._cells[y][x]
    queue = deque([cell])
    visited = set([cell])
    came_from = {}

    while queue:
        cell = queue.popleft()

        if cell._cord == exit:
            break

        availables = valid_directions(cell._cord, map)
        if availables:
            for available in availables:
                nx, ny = cell._neighbors[available]

                came_from[map._cells[ny][nx]] = cell

            nextCell = map._cells[y][x]
            queue.append(nextCell)
            queue.append(nextCell)
            map.print_matrix()
            pass


    # map.print_matrix()
    # map.write_hxmatrix("result.txt")
