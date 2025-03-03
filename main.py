from src.gameloop import GameLoop


VERSION = "1.1.2"


def main():
    print(f"Asteroid game ver {VERSION}")
    GameLoop().start(VERSION)
    


if __name__ == "__main__":
    main()