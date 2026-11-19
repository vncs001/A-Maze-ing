from maze import Matrix, Cell
import explorer

# LOGICA A*:
# - Explorer escolhe uma celula visinha entre as passagens disponiveis
# - Para escolher, cada vizinho tem uma pontuazao, priorizando aquela que parece oferecer o melhor caminho até a saída.
# - Essa pontuação é: f(n) = g(n) + h(n)
#           -> g(n): custo real para chegar até a posição atual, sendo cada movimento um custo. Ex: A -> B -> C: A=0, B=1, C=2
#           -> h(n): custo estimado da posição atual até o destino. Podendo usar distancia Manhattan: h(n) = |x_{exit}-x_n| + |y_{exit}-y_n|
#           -> f(n): custo estimado total do caminho passando por aquela posição.
# PASSOS:
#    1. Inicialização
#       [x] Identificar Entry e Exit.
#       [ ] Inicializar Open Set com Entry.
#       [ ] Inicializar Closed Set vazio.
#       [ ] Inicializar g_score com custo zero para Entry.
#       [ ] Inicializar came_from vazio.
#    2. Exploração
#    Enquanto Open Set não estiver vazio:
#       [ ] Retirar a célula com menor F.
#       [ ] Verificar se ela é a saída.
#       [ ] Se for, reconstruir o caminho.
#       [ ] Caso contrário, obter seus vizinhos.
#    3. Avaliação dos vizinhos
#    Para cada vizinho:
#       [ ] Verificar se está dentro dos limites.
#       [ ] Verificar se existe passagem entre as células.
#       [ ] Calcular o custo para chegar até ele.
#       [ ] Comparar com o custo conhecido anteriormente.
#       [ ] Se encontrou um caminho melhor, atualizar seu predecessor e seu custo.
#    4. Atualização
#       [ ] Adicionar o vizinho ao Open Set, caso ainda não esteja nele.
#    5. Finalização
#       [ ] Se o Open Set ficar vazio, significa que não existe caminho entre entrada e saída.
 
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
        if 0 <= nx < height and 0 <= ny < width:
            compass[direction] = not map._cells[ny][nx].visited #implementar para verificar se existe passagem
        else:
            compass[direction] = False

    available = [
        direction
        for direction, is_valid in compass.items()
            if is_valid
    ]
    return available

def a_star(entry: tuple[int, int], exit: tuple[int, int], map: Matrix):

