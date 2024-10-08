# Troll.py
from Monster import Monster

class Troll(Monster):
    def __init__(self):
        super().__init__("Troll", attack_power=40, defense=10, hp=150)
