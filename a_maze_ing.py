#!python3
import sys
from maze import Cell, Matrix


# Validar se o config.txt esta com tudo em ordem
def parser(file: str) -> dict:
    config: dict = []
    out_config: dict = {
        "WIDTH": 0,
        "HEIGHT": 0,
        "ENTRY": 0,
        "EXIT": 0,
        "OUTPUT_FILE": 0,
        "PERFECT": 0
    }
    converters = {
        "WIDTH": int,
        "HEIGHT": int,
        "ENTRY": lambda value: tuple(map(int, value.split(","))),
        "EXIT": lambda value: tuple(map(int, value.split(","))),
        "OUTPUT_FILE": str,
        "PERFECT": lambda value: value.lower() == "true"
    }
    with open(file, "r") as fl: 
        for line in fl:
            config.append(line.split("="))

    for key in out_config:
        valid: bool = False

        for key_conf, val_conf in config:
            if key == key_conf:
                valid = True
                out_config[key] = converters[key](val_conf.strip())

        if valid == False:
            raise ValueError(f"No key {key} in config file")

    return out_config


if __name__ == "__main__":
    print("-_-_- Starting -_-_-\n")
    try:
        # if len(sys.argv) != 2 or not sys.argv[1].endswith(".txt"):
        #     raise ValueError("Invalid input, usage: "
        #                      "python3 a_maze_ing.py config.txt")

        config = parser("config.txt")# "config.txt" ou sys.argv[1]
        if not config:
            raise ValueError("Invalid config file")

        # print(config["WIDTH"])
        matrix = Matrix(config["WIDTH"], config["HEIGHT"])
        matrix.build()
        matrix.print_matrix()

    except ValueError as e:
        print(f"Error - {e}")

    except FileNotFoundError:
        print(f"Error - File '{sys.argv[1]}' does not exist")
        sys.exit(1)

# MATRIX TESTER
    # matrix = Matrix(6, 6)
    # matrix.build()
    # matrix.print_matrix()
    # # Quebra uma parede
    # matrix._x_walls[0][4].break_wall()
    # print("==================================\n")
    # matrix.print_matrix()
    # # Reconstrói a parede e quebra uma a abaixo
    # matrix._x_walls[0][4].regenerate()
    # matrix._y_walls[0][4].break_wall()
    # print("==================================\n")
    # matrix.print_matrix()
