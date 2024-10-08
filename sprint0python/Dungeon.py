# Dungeon.py
import random
from Goblin import Goblin
from Orc import Orc
from Troll import Troll
from Treasure import Treasure

class Dungeon:
    def __init__(self, hero):
        self.hero = hero
        self.monsters = self.create_monsters()  # Crear monstruos aleatorios
        self.treasure = Treasure()

    def create_monsters(self):
        # Crear una lista de monstruos aleatorios
        monster_classes = [Goblin, Orc, Troll]
        return [random.choice(monster_classes)() for _ in range(3)]  # Crear 3 monstruos aleatorios

    def play(self):
        print("Hero enters the dungeon.")
        
        while self.monsters and self.hero.is_alive():
            current_monster = self.monsters[0]  # Get the first monster
            self.encounter_enemy(current_monster)

        if self.hero.is_alive():
            print(f"{self.hero.name} has defeated all monsters and conquered the dungeon!")
        else:
            print("The hero has fallen.")

    def encounter_enemy(self, monster):
        print(f"You have encountered a {monster.name}.")
        
        while monster.is_alive() and self.hero.is_alive():
            action = input("What do you want to do?\n1. Attack\n2. Defend\n3. Heal\nYour choice: ").strip()
            if action == "1":
                self.hero.attack(monster)
            elif action == "2":
                self.hero.defend()
            elif action == "3":
                self.hero.heal()
            else:
                print("Invalid option.")

            if monster.is_alive():
                monster.attack(self.hero)  # The monster attacks the hero

        if not monster.is_alive():
            self.monsters.remove(monster)  # Remove defeated monster
            print(f"{monster.name} has been defeated!")
            self.search_treasure()

    def search_treasure(self):
        print("Searching for treasure...")
        self.treasure.find_treasure(self.hero)  # The hero finds treasure
