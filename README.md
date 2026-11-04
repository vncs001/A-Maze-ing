# A-Maze-ing

# Material de apoio
- Teoria de grafos:
    https://www.youtube.com/watch?v=7wnAcDsckns

# DFS:
    -> monta a matriz com todas as paredes fechadas
    -> primeira celula escolhe uma parede da celula para quebrar e entrar no vizinho
    -> Continua ate entrar em uma celua sem vizinhos
    -> Quando chegar na sem vizinhos, volta uma celula pra tras e procura outra direcao

    PASSOS:
        -> montar uma matriz fechada
        -> classe celula deve guardar oq tem ao entorno, quais ja foram quebradas e se ja foi vizitada antes

    CELULA:
          N
        +---+       Deve ter as 4 direcoes e oq tem na outra direcao
      O |   | L     podendo ser: Outra celula ou nada. Caso tenha outra celula
        +---+       elas devem ter uma relacao, essa relacao e a parede, podendo
          S         estar quebrada ou inteira

    MATRIZ (6x6):
        
        +---+---+---+---+---+---+  x|__
 (0,0)->|   |   |   |   |   |   |    y 
        +---+---+---+---+---+---+
        |   |   |   |   |   |   |
        +---+---+---+---+---+---+
        |   |   |   |   |   |   |
        +---+---+---+---+---+---+
        |   |   |   |   |   |   |
        +---+---+---+---+---+---+
        |   |   |   |   |   |   |
        +---+---+---+---+---+---+
        |   |   |   |   |   |   |->(6,6)
        +---+---+---+---+---+---+



    def print_matrix(self):
        for y in range(self._height):
            for x in range(self._width):
                print(self._cells[y][x]._cord, end="")
                if x + 1 < self._width:
                    print(self._x_walls[y][x]._rep, end="")
            print("\n")
            for i in range(self._width):
                print(self._y_walls[i][x]._rep, end="")
            print("\n")