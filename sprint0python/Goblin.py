# Goblin.py
from Monster import Monster

class Goblin(Monster):
    def __init__(self):
        super().__init__("Goblin", attack_power=25, defense=5, hp=80)
