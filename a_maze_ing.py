#!
import sys

# Validar se o config.txt esta com tudo em ordem
def parser(file: str) -> dict:
    config: dict = []
    with open(file, "r") as fl:
        for line in fl:
            config.append(line.split("="))
    return config



if __name__ == "__main__":
    print("-_-_- Starting _-_-_")
    try:
        if not parser("config.txt"): #len(sys.argv) != 2 or sys.argv[1] != '*.txt' or 
            raise ValueError("Invalid input")


    except ValueError as e:
        print(f"Error - {e}")

