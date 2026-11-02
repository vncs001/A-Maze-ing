#!python3
import sys


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
    with open(file, "r") as fl: 
        for line in fl:
            config.append(line.split("="))

    for key in out_config:
        valid: bool = False

        for key_conf, val_conf in config:
            if key == key_conf:
                valid = True
                out_config[key] = val_conf

        if valid == False:
            raise ValueError(f"No key {key} in config file")

    return out_config


if __name__ == "__main__":
    print("-_-_- Starting _-_-_")
    try:
        #validador do config file e da usage
        if len(sys.argv) != 2 or not sys.argv[1].endswith(".txt"):
            raise ValueError("Invalid input, usage: "
                             "python3 a_maze_ing.py config.txt")

        config = parser(sys.argv[1])#"config.txt"
        if not config:
            raise ValueError("Invalid config file")
        print(config)

    except ValueError as e:
        print(f"Error - {e}")

    except FileNotFoundError:
        print(f"Error - File '{sys.argv[1]}' does not exist")
        sys.exit(1)

