# Treasure.py
import random

class Treasure:
    def __init__(self):
        # Lista de beneficios posibles
        self.benefits = [
            {"type": "increase_attack", "value": 10},
            {"type": "increase_defense", "value": 5},
            {"type": "restore_health", "value": 20}
        ]

    def find_treasure(self, hero):
        # Seleccionar un beneficio aleatorio
        benefit = random.choice(self.benefits)
        type = benefit["type"]
        value = benefit["value"]

        print(f"Hero has found a treasure: {type}.")
        
        # Aplicar el beneficio correspondiente
        if type == "increase_attack":
            hero.attack_power += value
            print(f"{hero.name}'s attack increases to {hero.attack_power}.")
        elif type == "increase_defense":
            hero.defense += value
            print(f"{hero.name}'s defense increases to {hero.defense}.")
        elif type == "restore_health":
            hero.hp += value
            if hero.hp > hero.hp_max:
                hero.hp = hero.hp_max
            print(f"{hero.name}'s health has been restored to {hero.hp}.")
