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

    MATRIZ:
        +---+---+---+---+
        |   |   |   |   |
        +---+---+---+---+
        |   |   |   |   |
        +---+---+---+---+
        |   |   |   |   |
        +---+---+---+---+
        |   |   |   |   |
        +---+---+---+---+
