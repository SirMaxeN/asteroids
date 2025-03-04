import asyncio
from src.gameloop import GameLoop


VERSION = "1.2.0"


async def main():
    print(f"Asteroid game ver {VERSION}")
    await GameLoop().start(VERSION)


if __name__ == "__main__":
    asyncio.run(main())
