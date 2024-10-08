from Hero import Hero
from Dungeon import Dungeon

if __name__ == "__main__":
    # Create the hero with a name passed as a parameter
    hero_name = input("Enter the name of your hero: ")
    hero = Hero(hero_name)

    # Create a dungeon with the hero
    dungeon = Dungeon(hero)

    # Start the game
    dungeon.play()
