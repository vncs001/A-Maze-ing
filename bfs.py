from maze import Matrix, Cell
from collections import deque


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
        if (0 <= nx < width and 0 <= ny < height) and (map._cells[ny][nx].valid):
            compass[direction] = not map._cells[y][x].has_wall(direction)# verifica se existe passagem pela direcao
        else:
            compass[direction] = False

    available = [
        direction
        for direction, is_valid in compass.items()
            if is_valid
    ]
    return available


def find_paths(queue: deque[Cell],
               visited: set[Cell],
               map: Matrix, exit: tuple[int, int]
               ) -> dict[tuple[int, int], tuple[tuple[int, int], str]]:

    came_from: dict[tuple[int, int], tuple[tuple[int, int], str]] = {}
    while queue:
        cell = queue.popleft()

        if cell._cord == exit:
            break

        availables = valid_directions(cell._cord, map)
        if availables:
            for available in availables:
                nx, ny = cell._neighbors[available]
                nextCell = map._cells[ny][nx]
                if nextCell in visited:
                    continue
                visited.add(nextCell)
                came_from[nextCell._cord] = (cell._cord, available)
                queue.append(nextCell)
    return came_from


def find_the_way(came_from: dict[tuple[int, int],
                    tuple[tuple[int, int], str]],
                    exit: tuple[int, int]
                    ) -> list[tuple[int, int]]:

    if exit not in came_from:
        return []

    path: list[tuple[int, int]] = []
    current = exit
    while current in came_from:
        path.append(current)
        cord, _ = came_from[current]
        current = cord

    path.append(current)
    path.reverse()
    return path


def bfs(entry: tuple[int, int], exit: tuple[int, int], map: Matrix):
    x, y = entry
    ex, ey = exit
    if not (0 <= x < map._width and 0 <= y < map._height):
        raise ValueError("Invalid init cell")
    
    if not (0 <= ex < map._width and 0 <= ey < map._height):
        raise ValueError("Invalid exit cell")

    cell = map._cells[y][x]
    queue = deque([cell])
    visited = set([cell])
    came_from = find_paths(queue, visited, map, exit)
    the_way = find_the_way(came_from, exit)
    return the_way
